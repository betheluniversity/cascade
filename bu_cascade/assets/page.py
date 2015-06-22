__author__ = 'ejc84332'

from asset import Asset
from structured_list import List

class Page(Asset):

    def __init__(self, ws_connector, identifier=None):
        super(self.__class__, self).__init__(ws_connector)
        self.asset_type = "page"
        self.identifier = identifier

    ## try that.
    def structured_data(self):
        return List(self.asset)

    def metadata(self):
        return List(self.asset['asset']['page']['metadata'])