__author__ = 'ejc84332'

import asset


class Page(asset.Asset):

    def __init__(self, ws_connector, identifier=None):
        super(self.__class__, self).__init__(ws_connector)
        self.asset_type = "page"
        self.identifier = identifier