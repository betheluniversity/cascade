from bu_cascade.assets.page import Page
from bu_cascade.assets.asset import Asset
from bu_cascade.cascade_connector import Cascade
import json

from config import SOAP_URL, CASCADE_LOGIN as AUTH, SITE_ID, TEST_PAGE_ID
ws_connector = Cascade(SOAP_URL, AUTH, SITE_ID)

# 1) get a created asset
my_page = Page(ws_connector, TEST_PAGE_ID)
asset = my_page.get_asset()

# 2) edit the same asset
asset['page']['metadata']['title'] = 'BANANA'
my_page.edit_asset(my_page.get_asset())

# 3) create a new asset
my_new_asset = Page(ws_connector, asset=asset)