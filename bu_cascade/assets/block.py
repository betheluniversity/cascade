__author__ = 'ces55739'

from asset import Asset
from structured_list import List

class Block(Asset):

    def __init__(self, ws_connector, identifier):
        super(self.__class__, self).__init__(ws_connector)
        self.asset_type = "block"
        self.identifier = identifier

    def structured_data(self):
        return List(self.asset['asset']['xhtmlDataDefinitionBlock'])

    # Todo: return the correct result
    # def metadata(self):
    #     return List(self.asset)