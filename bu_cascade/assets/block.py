__author__ = 'ces55739'

import asset


class Block(asset.Asset):

    def __init__(self, ws_connector, identifier):
        super(self.__class__, self).__init__(ws_connector)
        self.asset_type = "block"
        self.identifier = identifier
