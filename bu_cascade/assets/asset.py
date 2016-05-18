__author__ = 'ejc84332'


class Asset(object):

    def __init__(self, ws_connector, identifier):
        self.ws = ws_connector
        self.identifier = identifier
        self.asset_type = None
        self.asset = None

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, identifier):
        self.identifier = identifier

    def get_asset(self):
       return self.asset

    def set_asset(self, asset):
        self.asset =  asset

    def read_asset(self):
        read_asset = self.ws.read(self.identifier, self.asset_type)

        # convert Cascade Asset structure to a dict
        asset_structure = self.ws.build_asset_structure(read_asset)

        # if it was read correctly, get the asset
        if asset_structure['success'] == 'true':
            asset_structure = asset_structure['asset']

        self.set_asset(asset_structure)
        return asset_structure


    def create_asset(self, asset):
        return self.ws.create(asset)

    def edit_asset(self, asset):
        return self.ws.edit(asset)

    def delete_asset(self):
        return self.ws.delete(self.identifier, self.asset_type)

    def publish_asset(self):
        return self.ws.publish(self.identifier, self.asset_type)

    def unpublish_asset(self):
        return self.ws.unpublish(self.identifier, self.asset_type)

    def move_asset(self, folder_identifier):
        return self.ws.move(self.identifier, folder_identifier, self.asset_type)

    def rename_asset(self, new_name):
        return self.ws.rename(self.identifier, new_name, self.asset_type)

    def is_in_workflow_asset(self):
        return self.ws.is_in_workflow(self.identifier, self.asset_type)

