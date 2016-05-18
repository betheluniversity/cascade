__author__ = 'ejc84332'

from asset import Asset


class Page(Asset):

    def __init__(self, ws_connector, identifier=None, asset=None):
        super(self.__class__, self).__init__(ws_connector, identifier)
        self.asset_type = "page"
        self.identifier = identifier

        if identifier is not None:
            self.read_asset()
        elif asset is not None:
            self.create_asset(asset)
