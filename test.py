from bu_cascade.assets.page import Page
from bu_cascade.assets.block import Block
from bu_cascade.asset_tools import *
from bu_cascade.cascade_connector import Cascade
import json

from config import SOAP_URL, CASCADE_LOGIN as AUTH, SITE_ID, TEST_PAGE_ID, TEST_BLOCK_ID

ws_connector = Cascade(SOAP_URL, AUTH, SITE_ID)

print '--------------------  Start Test  ---------------------------'
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

    print find(page_md, 'title', False)
    print find(page_sd, 'group1', False)
    print find(page_sd, 'text2', False)
    print find(page_sd, 'text3', False)
    print find(page_sd, 'checkbox1', False)
    print find(page_sd, 'dropdown1', False)
    print find(page_sd, 'radio1', False)
    print find(page_sd, 'multiselect1', False)
    print find(page_sd, 'page-chooser', False)
    print find(page_sd, 'image-chooser', False)
    print find(page_sd, 'block-chooser', False)

    print '-----------'

    print find(page_md, 'title', True)
    print find(page_sd, 'group1', True)
    print find(page_sd, 'text2', True)
    print find(page_sd, 'text3', True)
    print find(page_sd, 'checkbox1', True)
    print find(page_sd, 'dropdown1', True)
    print find(page_sd, 'radio1', True)
    print find(page_sd, 'multiselect1', True)
    print find(page_sd, 'page-chooser', True)
    print find(page_sd, 'image-chooser', True)
    print find(page_sd, 'block-chooser', True)

############################ Asset Tools -- Find() ############################
def test_update():
    my_page = Page(ws_connector, TEST_PAGE_ID)
    page_asset, page_md, page_sd = my_page.get_asset()

    print update(page_md, 'title', 'CALEBasdfasdf')
    print update(page_md, 'school', ['Bethel University', 'College of Arts & Sciences'])

    print update(page_sd, 'date1', '06-01-2016')
    print update(page_sd, 'text2', 'CALEB')
    print update(page_sd, 'text3', 'CALEB')
    print update(page_sd, 'checkbox1', ['CALEB', 'Yes1'])
    print update(page_sd, 'dropdown1', 'CALEB')
    print update(page_sd, 'radio1', 'Yes')
    print update(page_sd, 'multiselect1', ['test', 'test2'])
    # print update(page_sd, 'page-chooser', 'CALEB')
    # print update(page_sd, 'image-chooser', 'CALEB')
    # print update(page_sd, 'block-chooser', 'CALEB')

    print my_page.edit_asset(page_asset)

###################### Testing area to call functions #####################

##########################################################################
print '---------------------  Finished Test  --------------------------'