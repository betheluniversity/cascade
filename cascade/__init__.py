from cascade_connector import Cascade
from assets.page import Page

wsdl = "http://cms-origin.bethel.edu/ws/services/AssetOperationService"
auth = {'username': 'tinker', 'password': 'v3rQWaJZorT2pAJ'}
site_id = 'ba134ac58c586513100ee2a7cec27f4a'
cascade = Cascade(wsdl, auth, site_id)