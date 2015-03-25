from suds.client import Client
from suds.transport import TransportError


class Cascade(object):

    def __init__(self, service_url, login, site_id):
        self.service_url = service_url
        self.login = login
        self.site_id = site_id
        self.client = self.get_client()

    def get_client(self):
        try:
            client = Client(url=self.service_url+'?wsdl', location=self.service_url)
            return client
        except TransportError:
            return None

    def read(self, path_or_id, asset_type):
        identifier = Cascade.create_identifier(self, path_or_id, asset_type)

        response = self.client.service.read(self.login, identifier)
        return response

    def create(self, asset):
        response = self.client.service.create(self.login, asset)
        return response

    def edit(self, asset):
        response = self.client.service.edit(self.login, asset)
        return response

    def delete(self, path_or_id, asset_type):
        identifier = Cascade.create_identifier(self, path_or_id, asset_type )
        response = self.client.service.delete(self.login, identifier)
        return response

    def create_identifier(self, path_or_id, asset_type):
        if path_or_id is None:
            return None
        if path_or_id[0] == "/":
            identifier = {
                'type': asset_type,
                'path': {
                    'path': path_or_id,
                    'siteId': self.site_id
                }
            }
        else:
            identifier = {
                'id': path_or_id,
                'type': asset_type,
            }

        return identifier

    # Additional potential methods

    # def publish(self, path_or_id, asset_type):
    #     identifier = Cascade.create_identifier(self, path_or_id, asset_type)
    #     identifier = {
    #         "identifier": identifier
    #     }
    #
    #     response = self.client.service.publish(self.login, identifier)
    #     return response
    #
    # def unpublish(self, path_or_id, asset_type):
    #     identifier = Cascade.create_identifier(self, path_or_id, asset_type)
    #     identifier = {
    #         "identifier": identifier,
    #         "unpublish": True
    #     }
    #
    #     response = self.client.service.publish(self.login, identifier)
    #     return response
    #
    # def move(self, old_path_or_id, new_path_or_id, asset_type):
    #     identifier = Cascade.create_identifier(self, old_path_or_id, asset_type )
    #     new_identifier = Cascade.create_identifier(self, new_path_or_id, asset_type )
    #
    #     moveParameters = {
    #         "destinationContainerIdentifier": new_identifier,
    #         "doWorkFlow": False,
    #     }
    #
    #     response = self.client.service.move(self.login, identifier, moveParameters)
    #     return response
    #
    # def rename(self, path_or_id, new_name, asset_type):
    #     identifier = Cascade.create_identifier(self, path_or_id, asset_type )
    #
    #     renameParameters = {
    #         "doWorkFlow": False,
    #         "newName": new_name
    #     }
    #
    #     # Note: rename is the same call as move, with different parameters
    #     response = self.client.service.move(self.login, identifier, renameParameters)
    #     return response
    #
    # def is_asset_currently_in_workflow(self, path_or_id, asset_type):
    #     identifier = Cascade.create_identifier(self, path_or_id, asset_type )
    #
    #     response = self.client.service.readWorkflowInformation(self.login, identifier)
    #
    #     if response.workflow is not None:
    #         if str(response.workflow.currentStep) != "finish":
    #             return True
    #
    #     return False

