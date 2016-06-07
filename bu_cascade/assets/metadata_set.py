__author__ = 'ces55739'

from asset import Asset


class MetadataSet(Asset):

    def __init__(self, ws_connector, identifier=None, asset=None):
        super(self.__class__, self).__init__(ws_connector, identifier, asset_type='metadataset', asset_specific_key='metadataSet')

        if identifier is not None:
            self.read_asset()
        elif asset is not None:
            self.create_asset(asset)
