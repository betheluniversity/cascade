import os
import sys
from copy import deepcopy
from datetime import datetime
from pathlib import Path

import pytest

# Make src-layout imports work when running pytest from the repository root.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
USE_INSTALLED_PACKAGE = os.getenv("CASCADE_USE_INSTALLED_PACKAGE", "0").strip().lower() in ("1", "true", "yes")
if not USE_INSTALLED_PACKAGE:
    sys.path.insert(0, str(SRC_DIR))

try:
    from bu_cascade.asset_tools import find, update, update_data_definition, update_metadata_set
    from bu_cascade.assets.block import Block
    from bu_cascade.assets.data_definition import DataDefinition
    from bu_cascade.assets.metadata_set import MetadataSet
    from bu_cascade.assets.page import Page
    from bu_cascade.cascade_connector import Cascade
except Exception as exc:
    pytest.skip(f"bu_cascade import failed in this environment: {exc}", allow_module_level=True)

try:
    from config import CASCADE_LOGIN as AUTH
    from config import SITE_ID, SOAP_URL, STAGING_DESTINATION_ID
except ImportError as exc:
    pytest.skip(f"config.py is required for live Cascade integration tests: {exc}", allow_module_level=True)

TEST_ROOT_FOLDER_PATH = "/_testing/bu-cascade"
TEST_BASE_ASSETS_FOLDER_PATH = TEST_ROOT_FOLDER_PATH + "/base-assets"
TEST_PARENT_FOLDER_PATH = TEST_ROOT_FOLDER_PATH + "/runtime"
TEST_PAGE_CHOOSER_PATH = TEST_ROOT_FOLDER_PATH + "/major-minor"
TEST_PAGE_ID = "7913f3cf0a64654909e203bc8e53ec09"
TEST_BLOCK_ID = "798597480a64654909e203bcfcd6be7d"
TEST_PROGRAM_BLOCK_ID = "798597480a64654909e203bcfcd6be7d"
TEST_FACULTY_PAGE_ID = "798a19ab0a64654909e203bc1f7398fe"
TEST_METADATA_SET_ID = "7922fcf10a64654909e203bc81ccb38e"
TEST_DATA_DEFINITION_ID = "7926a95a0a64654909e203bc926f39a2"


pytestmark = pytest.mark.integration


def _unique_name(prefix):
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
    return "{}-{}".format(prefix, timestamp)


def _assert_created_asset_response(response, label):
    if isinstance(response, dict):
        created_id = response.get("createdAssetId")
    else:
        created_id = getattr(response, "createdAssetId", None)
    assert created_id, "{} create returned no createdAssetId. Response: {}".format(label, response)


def _prepare_page_for_create(page_asset, name_prefix):
    new_page_asset = deepcopy(page_asset)
    page = new_page_asset["page"]
    page["id"] = None
    page["path"] = None
    page["parentFolderId"] = None
    page["parentFolderPath"] = TEST_PARENT_FOLDER_PATH
    page["name"] = _unique_name(name_prefix)
    return new_page_asset


def _prepare_block_for_create(block_asset, name_prefix):
    new_block_asset = deepcopy(block_asset)
    block = new_block_asset["xhtmlDataDefinitionBlock"]
    block["id"] = None
    block["path"] = None
    block["parentFolderId"] = None
    block["parentFolderPath"] = TEST_PARENT_FOLDER_PATH
    block["name"] = _unique_name(name_prefix)
    return new_block_asset


def _skip_if_base_asset(asset, asset_key, id_name):
    path = asset.get(asset_key, {}).get("path")
    if isinstance(path, bytes):
        path = path.decode("utf-8")
    if path and path.startswith(TEST_BASE_ASSETS_FOLDER_PATH):
        pytest.skip(
            "{} points to {}. Use an ID under {} for destructive edit tests.".format(
                id_name, TEST_BASE_ASSETS_FOLDER_PATH, TEST_PARENT_FOLDER_PATH
            )
        )


def _require_id(value, name):
    if not value:
        pytest.skip(f"Set {name} in tests/test.py to run this integration test")


@pytest.fixture(scope="module")
def ws_connector():
    connector = Cascade(SOAP_URL, AUTH, SITE_ID, STAGING_DESTINATION_ID)
    if connector.client is None:
        pytest.skip("Could not connect to Cascade SOAP service")
    return connector


@pytest.fixture
def my_page(ws_connector):
    _require_id(TEST_PAGE_ID, "TEST_PAGE_ID")
    page = Page(ws_connector, TEST_PAGE_ID)
    page_asset, _page_md, _page_sd = page.get_asset()
    _skip_if_base_asset(page_asset, "page", "TEST_PAGE_ID")
    return page


@pytest.fixture
def my_block(ws_connector):
    _require_id(TEST_BLOCK_ID, "TEST_BLOCK_ID")
    block = Block(ws_connector, TEST_BLOCK_ID)
    block_asset, _block_md, _block_sd = block.get_asset()
    _skip_if_base_asset(block_asset, "xhtmlDataDefinitionBlock", "TEST_BLOCK_ID")
    return block


@pytest.fixture
def page_asset(my_page):
    asset, _md, _sd = my_page.get_asset()
    return asset


@pytest.fixture
def block_asset(my_block):
    asset, _md, _sd = my_block.get_asset()
    return asset


def test_page_read(my_page):
    page_asset, page_md, page_sd = my_page.get_asset()
    assert page_asset is not None
    assert page_md is not None
    assert page_sd is not None


@pytest.mark.destructive
def test_page_edit(my_page):
    page_asset, page_md, _page_sd = my_page.get_asset()
    page_md["title"] = "Test"
    response = my_page.edit_asset(page_asset)
    assert response is not None


@pytest.mark.destructive
def test_page_create(ws_connector, page_asset):
    new_page_asset = _prepare_page_for_create(page_asset, "created-from-page-asset")
    created = ws_connector.create(new_page_asset)
    _assert_created_asset_response(created, "page")


def test_block_read(my_block):
    block_asset, block_md, block_sd = my_block.get_asset()
    assert block_asset is not None
    assert block_md is not None
    assert block_sd is not None


@pytest.mark.destructive
def test_block_edit(my_block):
    block_asset, block_md, _block_sd = my_block.get_asset()
    block_md["title"] = "Test"
    response = my_block.edit_asset(block_asset)
    assert response is not None


@pytest.mark.destructive
def test_block_create(ws_connector, block_asset):
    new_block_asset = _prepare_block_for_create(block_asset, "created-from-block-asset")
    created = ws_connector.create(new_block_asset)
    _assert_created_asset_response(created, "block")


def test_base_asset_get(ws_connector):
    new_page_asset, _new_page_md, _new_page_sd = ws_connector.load_base_asset_by_id(
        "ba13b3a18c586513100ee2a7ca94e2f2", "page"
    )
    new_block_asset, _new_block_md, _new_block_sd = ws_connector.load_base_asset_by_id(
        "ba1380b08c586513100ee2a7d238e036", "block"
    )
    assert new_page_asset is not None
    assert new_block_asset is not None


@pytest.mark.destructive
def test_base_asset_create(ws_connector):
    new_page_asset, _new_page_md, _new_page_sd = ws_connector.load_base_asset_by_id(
        "ba13b3a18c586513100ee2a7ca94e2f2", "page"
    )
    new_page_asset = _prepare_page_for_create(new_page_asset, "created-from-base-asset")
    created = ws_connector.create(new_page_asset)
    _assert_created_asset_response(created, "base page")


def test_find(my_page):
    _page_asset, page_md, page_sd = my_page.get_asset()

    assert find(page_md, "title", False) is not None

    # These fields vary by content type, so we only verify helper behavior for existing keys.
    existing_group = find(page_sd, "group1", True)
    if existing_group is not None:
        assert find(page_sd, "group1", False) is not None


@pytest.mark.destructive
def test_update_page_a(my_page):
    page_asset, _page_md, page_sd = my_page.get_asset()
    update(page_sd, "send-email", "Newer Value")
    response = my_page.edit_asset(page_asset)
    assert response is not None


@pytest.mark.destructive
def test_update_page_c(my_page):
    page_asset, page_md, page_sd = my_page.get_asset()

    assert update(page_asset, "title", "CALEB") is not None
    assert update(page_md, "checkbox", "4") is not None
    assert update(page_md, "dropdown", "asdf") is not None
    assert update(page_md, "multiselect", "5") is not None
    assert update(page_md, "radio2", "2") is not None
    assert update(page_md, "text", "new test") is not None

    assert update(page_sd, "date1", "06-07-2016") is not None
    assert update(page_sd, "text2", "new test2") is not None
    assert update(page_sd, "text3", "new test3") is not None
    assert update(page_sd, "checkbox1", "asdf") is not None
    assert update(page_sd, "dropdown1", "2") is not None
    assert update(page_sd, "radio1", "3") is not None
    assert update(page_asset, "multiselect1", ["4", "asdf"]) is not None
    assert update(page_sd, "page-chooser", TEST_PAGE_CHOOSER_PATH) is not None

    response = my_page.edit_asset(page_asset)
    assert response is not None


@pytest.mark.destructive
def test_update_multiple_block(ws_connector):
    _require_id(TEST_PROGRAM_BLOCK_ID, "TEST_PROGRAM_BLOCK_ID")
    my_block = Block(ws_connector, TEST_PROGRAM_BLOCK_ID)
    block_asset, _block_md, block_sd = my_block.get_asset()
    _skip_if_base_asset(block_asset, "xhtmlDataDefinitionBlock", "TEST_PROGRAM_BLOCK_ID")

    concentrations = {
        "concentration": {
            "concentration_code": "lol",
            "concentration_description": "dota",
            "total_credits": "11",
            "program_length": "2",
            "courses": [
                {
                    "course_heading": "TEST1a",
                    "description": "TEST1b",
                    "course_numbers": "TEST1c",
                },
                {
                    "course_heading": "TEST2a",
                    "description": "TEST2b",
                    "course_numbers": "TEST2c",
                },
            ],
        }
    }
    for key, value in concentrations.items():
        update(block_sd, key, value)

    response = my_block.edit_asset(block_asset)
    assert response is not None


@pytest.mark.destructive
def test_update_multiple_page(ws_connector):
    _require_id(TEST_FACULTY_PAGE_ID, "TEST_FACULTY_PAGE_ID")
    my_page = Page(ws_connector, TEST_FACULTY_PAGE_ID)
    page_asset, _page_md, page_sd = my_page.get_asset()
    _skip_if_base_asset(page_asset, "page", "TEST_FACULTY_PAGE_ID")

    bio = {
        "job-title": [
            "first job title",
            "2nd job title",
            "3rd job title",
        ]
    }

    for key, value in bio.items():
        update(page_sd, key, value)

    response = my_page.edit_asset(page_asset)
    assert response is not None


@pytest.mark.destructive
def test_update_metadata_set(ws_connector):
    _require_id(TEST_METADATA_SET_ID, "TEST_METADATA_SET_ID")
    asset = MetadataSet(ws_connector, TEST_METADATA_SET_ID)
    metadata_asset, _unused_1, _unused_2 = asset.get_asset()

    assert update_metadata_set(metadata_asset, "radio1", ["1", "asdf"], "asdf") is not None
    assert update_metadata_set(metadata_asset, "radio2", ["2", "asdf"]) is not None
    assert update_metadata_set(metadata_asset, "dropdown", ["3", "asdf"]) is not None
    assert update_metadata_set(metadata_asset, "checkbox", ["4", "asdf"]) is not None
    assert update_metadata_set(metadata_asset, "multiselect", ["5", "asdf"]) is not None

    response = asset.edit_asset(metadata_asset)
    assert response is not None


@pytest.mark.destructive
def test_update_data_definition(ws_connector):
    _require_id(TEST_DATA_DEFINITION_ID, "TEST_DATA_DEFINITION_ID")
    asset = DataDefinition(ws_connector, TEST_DATA_DEFINITION_ID)
    data_definition_asset, _unused_1, _unused_2 = asset.get_asset()

    assert update_data_definition(data_definition_asset, "school", ["1", "asdf", "another", "TEST"]) is not None
    assert update_data_definition(data_definition_asset, "dropdown1", ["2", "asdf"]) is not None
    assert update_data_definition(data_definition_asset, "radio1", ["3", "asdf"]) is not None
    assert update_data_definition(data_definition_asset, "multiselect1", ["4", "asdf"]) is not None

    response = asset.edit_asset(data_definition_asset)
    assert response is not None


@pytest.mark.destructive
def test_event(my_page):
    page_asset, _page_md, page_sd = my_page.get_asset()
    current_value = find(page_sd, "event-dates", False)
    if current_value is None:
        pytest.skip("event-dates field not present on test page")

    assert update(page_sd, "event-dates", [{"start-date": 1468006951000, "end-date": 1468006951000}]) is not None

    response = my_page.edit_asset(page_asset)
    assert response is not None
