from bu_cascade.assets.page import Page
from bu_cascade.assets.block import Block
from bu_cascade.assets.asset import Asset
from bu_cascade.cascade_connector import Cascade
import json

from config import SOAP_URL, CASCADE_LOGIN as AUTH, SITE_ID, TEST_PAGE_ID, TEST_BLOCK_ID

ws_connector = Cascade(SOAP_URL, AUTH, SITE_ID)

############################ Page ########################################
# 1a) read
my_page = Page(ws_connector, TEST_PAGE_ID)
page_asset, page_md, page_sd = my_page.get_asset()

# b) edit
page_md['title'] = 'Test'
my_page.edit_asset(page_asset)

# c) create
# my_new_page = Page(ws_connector, asset=page_asset)

############################ Block ########################################
# 2a) read
my_block = Block(ws_connector, TEST_BLOCK_ID)
block_asset, block_md, block_sd = my_block.get_asset()

# 2b) edit
block_md['title'] = 'Test'
my_block.edit_asset(block_asset)

# 2c) create
# my_new_block = Block(ws_connector, asset=block_asset)

############################ Load Base Assets ############################

# 3a) grabbing base assets
new_page_asset, new_page_md, new_page_sd = ws_connector.load_base_asset_by_id('ba13b3a18c586513100ee2a7ca94e2f2', 'page')
new_block_asset, new_block_md, new_block_sd = ws_connector.load_base_asset_by_id('ba1380b08c586513100ee2a7d238e036', 'block')

# 3b) create new asset from a base asset
# new_page_asset['page']['parentFolderPath'] = '/_testing/caleb-schwarze/testing-bu-cascade'
# new_page_asset['page']['name'] = 'created-from-base-asset'
# Page(ws_connector, asset=new_page_asset)

##########################################################################
print "Finished Test"