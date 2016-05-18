from bu_cascade.assets.page import Page
from bu_cascade.assets.block import Block
from bu_cascade.assets.asset import Asset
from bu_cascade.cascade_connector import Cascade
import json

from config import SOAP_URL, CASCADE_LOGIN as AUTH, SITE_ID, TEST_PAGE_ID, TEST_BLOCK_ID
ws_connector = Cascade(SOAP_URL, AUTH, SITE_ID)

# 1a) get a created page with asset, metadata, and structured data
my_page = Page(ws_connector, TEST_PAGE_ID)
page_asset, page_md, page_sd = my_page.get_asset()

# b) edit the same asset
page_md['title'] = 'Test'
my_page.edit_asset(page_asset)

# c) create a new asset
# my_new_page = Page(ws_connector, asset=page_asset)

# 2a) get a created block with asset, metadata, and structured data
my_block = Block(ws_connector, TEST_BLOCK_ID)
block_asset, block_md, block_sd = my_block.get_asset()

# 2b)
block_md['title'] = 'Test'
my_block.edit_asset(block_asset)

# 2c)
# my_new_block = Block(ws_connector, asset=block_asset)
