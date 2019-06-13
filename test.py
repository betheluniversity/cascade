from bu_cascade.assets.page import Page
from bu_cascade.assets.block import Block
from bu_cascade.assets.metadata_set import MetadataSet
from bu_cascade.assets.data_definition import DataDefinition
from bu_cascade.asset_tools import *
from bu_cascade.cascade_connector import Cascade
import json

from config import SOAP_URL, CASCADE_LOGIN as AUTH, SITE_ID, TEST_PAGE_ID, TEST_BLOCK_ID, TEST_PROGRAM_BLOCK_ID, TEST_FACULTY_PAGE_ID, TEST_METADATA_SET_ID, TEST_DATA_DEFINITION_ID, STAGING_DESTINATION_ID

ws_connector = Cascade(SOAP_URL, AUTH, SITE_ID, STAGING_DESTINATION_ID)

print('--------------------  Start Test  ---------------------------')
############################ Page ########################################
# 1a) read
def test_page_read():
    my_page = Page(ws_connector, TEST_PAGE_ID)
    page_asset, page_md, page_sd = my_page.get_asset()
    return page_asset, page_md, page_sd

# b) edit
def test_page_edit(my_page):
    page_asset, page_md, page_sd = my_page.get_asset()
    page_md['title'] = 'Test'
    return my_page.edit_asset(page_asset)

# c) create
def test_page_create(page_asset):
    return Page(ws_connector, asset=page_asset)

############################ Block ########################################
# 2a) read
def test_block_read():
    my_block = Block(ws_connector, TEST_BLOCK_ID)
    block_asset, block_md, block_sd = my_block.get_asset()
    return block_asset, block_md, block_sd

# 2b) edit
# Todo: use Asset Tools -- find and update
def test_block_edit(my_block):
    block_asset, block_md, block_sd = my_block.get_asset()
    block_md['title'] = 'Test'
    return my_block.edit_asset(block_asset)

# 2c) create
def test_block_create(block_asset):
    return Block(ws_connector, asset=block_asset)

############################ Load Base Assets ############################

# 3a) grabbing base assets
def test_base_asset_get():
    new_page_asset, new_page_md, new_page_sd = ws_connector.load_base_asset_by_id('ba13b3a18c586513100ee2a7ca94e2f2', 'page')
    new_block_asset, new_block_md, new_block_sd = ws_connector.load_base_asset_by_id('ba1380b08c586513100ee2a7d238e036', 'block')
    return new_block_asset

# 3b) create new asset from a base asset
def test_base_asset_create(new_page_asset):
    new_page_asset['page']['parentFolderPath'] = '/_testing/caleb-schwarze/testing-bu-cascade'
    new_page_asset['page']['name'] = 'created-from-base-asset'
    Page(ws_connector, asset=new_page_asset)

############################ Asset Tools -- Find() ############################
def test_find():
    page_asset, page_md, page_sd = test_page_read()

    print(find(page_md, 'title', False))
    print(find(page_sd, 'group1', False))
    print(find(page_sd, 'text2', False))
    print(find(page_sd, 'text3', False))
    print(find(page_sd, 'checkbox1', False))
    print(find(page_sd, 'dropdown1', False))
    print(find(page_sd, 'radio1', False))
    print(find(page_sd, 'multiselect1', False))
    print(find(page_sd, 'page-chooser', False))
    print(find(page_sd, 'image-chooser', False))
    print(find(page_sd, 'block-chooser', False))

    print('-----------')

    print(find(page_md, 'title', True))
    print(find(page_sd, 'group1', True))
    print(find(page_sd, 'text2', True))
    print(find(page_sd, 'text3', True))
    print(find(page_sd, 'checkbox1', True))
    print(find(page_sd, 'dropdown1', True))
    print(find(page_sd, 'radio1', True))
    print(find(page_sd, 'multiselect1', True))
    print(find(page_sd, 'page-chooser', True))
    print(find(page_sd, 'image-chooser', True))
    print(find(page_sd, 'block-chooser', True))

############################ Asset Tools -- Update() #1 ############################
def test_update_page():
    my_page = Page(ws_connector, TEST_PAGE_ID)
    page_asset, page_md, page_sd = my_page.get_asset()

    # basic md
    print(update(page_asset, 'title', 'CALEB'))

    # dynamic md
    print(update(page_md, 'checkbox', '4'))
    print(update(page_md, 'dropdown', 'asdf'))
    print(update(page_md, 'multiselect', '5'))
    print(update(page_md, 'radio2', '2'))
    print(update(page_md, 'text', 'new test'))

    # structured data
    print(update(page_sd, 'date1', '06-07-2016'))
    print(update(page_sd, 'text2', 'new test2'))
    print(update(page_sd, 'text3', 'new test3'))
    print(update(page_sd, 'checkbox1', 'asdf'))
    print(update(page_sd, 'dropdown1', '2'))
    print(update(page_sd, 'radio1', '3'))
    print(update(page_asset, 'multiselect1', ['4', 'asdf']))
    print(update(page_sd, 'page-chooser', '/_testing/caleb-schwarze/major-minor'))




    # print(update(page_sd, 'image-chooser', 'CALEB2'))
    # print(update(page_sd, 'block-chooser', '/CALEB2'))

    print(my_page.edit_asset(page_asset))

############################ Asset Tools -- Update() #2 ############################
def test_update_multiple_block():
    my_block = Block(ws_connector, TEST_PROGRAM_BLOCK_ID)
    block_asset, block_md, block_sd = my_block.get_asset()

    concentrations = {
        'concentration': {
            'concentration_code': 'lol',
            'concentration_description': 'dota',
            'total_credits': '11',
            'program_length': '2',

            'courses': [
                {
                    'course_heading': 'TEST1a',
                    'description': 'TEST1b',
                    'course_numbers': 'TEST1c'
                },
                {
                    'course_heading': 'TEST2a',
                    'description': 'TEST2b',
                    'course_numbers': 'TEST2c'
                }
            ]
        }
    }
    print(concentrations)
    for key, value in concentrations.items():
        update( block_sd, key, value)


    block_asset2, block_md2, block_sd2 = my_block.get_asset()
    my_block.edit_asset(block_asset2)


def test_update_multiple_page():
    my_page = Page(ws_connector, TEST_FACULTY_PAGE_ID)
    page_asset, page_md, page_sd, = my_page.get_asset()

    bio = {
        'job-title': [
            'first job title',
            '2nd job title',
            '3rd job title'
        ]
    }

    for key, value in bio.items():
        update( page_sd, key, value)

    page_asset2, page_md2, page_sd2 = my_page.get_asset()
    my_page.edit_asset(page_asset2)


def test_update_metadata_set():
    asset = MetadataSet(ws_connector, TEST_METADATA_SET_ID)
    metadata_asset, empty_variable, empty_variable = asset.get_asset()

    update_metadata_set(metadata_asset, 'radio1', ['1', 'asdf'], 'asdf')
    update_metadata_set(metadata_asset, 'radio2', ['2', 'asdf'])
    update_metadata_set(metadata_asset, 'dropdown', ['3', 'asdf'])
    update_metadata_set(metadata_asset, 'checkbox', ['4', 'asdf'])
    update_metadata_set(metadata_asset, 'multiselect', ['5', 'asdf'])

    asset.edit_asset(metadata_asset)


def test_update_data_definition():
    asset = DataDefinition(ws_connector, '30fd148b8c58651305d792995121ee73')
    data_definition_asset, empty_variable, empty_variable = asset.get_asset()

    update_data_definition(data_definition_asset, 'school', ['1', 'asdf', 'another', 'TEST'])
    update_data_definition(data_definition_asset, 'dropdown1', ['2', 'asdf'])
    update_data_definition(data_definition_asset, 'radio1', ['3', 'asdf'])
    update_data_definition(data_definition_asset, 'multiselect1', ['4', 'asdf'])

    asset.edit_asset(data_definition_asset)

def test_event():
    my_page = Page(ws_connector, 'cc0396008c58651305d7929990ca7750')
    page_asset, page_md, page_sd, = my_page.get_asset()

    print(find(page_sd, 'event-dates', False))
    print(update(page_sd, 'event-dates', [{'start-date': 1468006951000, 'end-date': 1468006951000}]))

    print(my_page.edit_asset(page_asset))

###################### Testing area to call functions #####################
# print(test_page_read())
##########################################################################
print('---------------------  Finished Test  --------------------------')