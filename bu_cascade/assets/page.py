__author__ = 'ejc84332'

import asset


class Page(asset.Asset):

    def __init__(self, ws_connector):
        super(self.__class__, self).__init__(ws_connector)
