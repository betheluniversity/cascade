__author__ = 'ejc84332'


class Asset(object):

    def __init__(self, ws_connector, identifier=None):
        self.ws = ws_connector
        self.identifier = identifier

    def set_identifier(self, identifier):
        self.identifier = identifier

    def read_asset(self, identifier=None):
        # can either set identifier on creation or when you call read_asset
        if self.identifier is not None:
            self.set_identifier(self.identifier)
        else:
            self.set_identifier(identifier)

        asset = self.ws.read(self.identifier, self.asset_type)

        # set the asset value to the writable asset structure
        self.asset = self.get_asset_structure(asset)

        return asset

    def create_asset(self, asset):
        return self.ws.create(asset)

    def edit_asset(self, asset):
        return self.ws.edit(asset)

    def delete_asset(self, identifier=None):
        if identifier:
            self.set_identifier(identifier)
        return self.ws.delete(self.identifier, self.asset_type)

    # Dynamically builds the asset into a writable structure
    def get_asset_structure(asset):
        asset = {}

        # Get metadata/dynamic-fields/etc


        # Build asset structure


        return asset

    # Additional potential methods

    # def publish_asset(self, identifier=None):
    #     if identifier:
    #         self.set_identifier(identifier)
    #     return self.ws.publish(self.identifier, self.asset_type)
    #
    # def unpublish_asset(self, identifier=None):
    #     if identifier:
    #         self.set_identifier(identifier)
    #     return self.ws.unpublish(self.identifier, self.asset_type)
    #
    # def move(self, identifier=None, new_identifier=None):
    #     if identifier:
    #         self.set_identifier(identifier)
    #     return self.ws.move(self.identifier, new_identifier, self.asset_type)
    #
    # def rename(self, identifier=None, new_name=None):
    #     if identifier:
    #         self.set_identifier(identifier)
    #     return self.ws.rename(self.identifier, new_name, self.asset_type)

