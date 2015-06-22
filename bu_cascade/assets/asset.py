__author__ = 'ejc84332'
import json
from structured_list import List

class Asset(object):

    def __init__(self, ws_connector, identifier=None):
        self.ws = ws_connector
        self.identifier = identifier
        self.asset_type = None
        self.asset = {}

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, identifier):
        self.identifier = identifier

    def get_asset(self):
       return self.asset

    def set_asset(self, asset):
        self.asset =  asset

    def read_asset(self, identifier=None):
        if self.identifier is None:
            self.set_identifier(identifier)
        else:
            identifier = self.identifier

        read_asset = self.ws.read(self.identifier, self.asset_type)

        # set the asset value to the writable asset structure
        asset_structure = json.loads(self.ws.build_asset_structure(read_asset))

        self.set_asset(asset_structure)

        return asset_structure

    def create_asset(self, asset):
        return self.ws.create(asset)

    def edit_asset(self, asset=None):
        if asset is None:
            asset = self.asset
        return self.ws.edit(asset)

    def delete_asset(self, identifier=None):
        if identifier:
            self.set_identifier(identifier)
        return self.ws.delete(self.identifier, self.asset_type)

    def publish_asset(self, identifier=None):
        if identifier:
            self.set_identifier(identifier)
        return self.ws.publish(self.identifier, self.asset_type)

    def unpublish_asset(self, identifier=None):
        if identifier:
            self.set_identifier(identifier)
        return self.ws.unpublish(self.identifier, self.asset_type)

    def move_asset(self, new_identifier=None, identifier=None):
        if identifier:
            old_identifier = identifier
        else:
            old_identifier = self.identifier

        if new_identifier:
            self.set_identifier((new_identifier))
        return self.ws.move(self.identifier, old_identifier, self.asset_type)

    def rename_asset(self, identifier, new_name):
        if identifier:
            self.set_identifier((identifier))

        return self.ws.rename(self.identifier, new_name, self.asset_type)

    def is_in_workflow_asset(self, identifier=None):
        if identifier:
            self.set_identifier(identifier)
        return self.ws.is_in_workflow(self.identifier, self.asset_type)

    ## Test functions