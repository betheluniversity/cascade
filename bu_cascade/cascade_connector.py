from suds.client import Client
from suds.transport import TransportError
import json


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
        identifier = self.create_identifier(path_or_id, asset_type)

        response = self.client.service.read(self.login, identifier)
        return response

    def create(self, asset):
        response = self.client.service.create(self.login, asset)
        return response

    def edit(self, asset):
        response = self.client.service.edit(self.login, asset)
        return response

    def delete(self, path_or_id, asset_type):
        identifier = self.create_identifier(path_or_id, asset_type)
        response = self.client.service.delete(self.login, identifier)
        return response

    # Dynamically builds the asset into a writable structure
    def build_asset_structure(self, asset):
        asset = self.suds_to_json(asset)

        return asset

    def suds_to_json(self, data):
        return json.dumps(self.recursive_asdict(data))

    def recursive_asdict(self, d):
        from suds.sudsobject import asdict

        """Convert Suds object into serializable format."""
        out = {}
        for k, v in asdict(d).iteritems():
            if hasattr(v, '__keylist__'):
                out[k] = self.recursive_asdict(v)
            elif isinstance(v, list):
                out[k] = []
                for item in v:
                    if hasattr(item, '__keylist__'):
                        out[k].append(self.recursive_asdict(item))
                    else:
                        out[k].append(item)

            else:
                # if it has hour, format it correctly as a date
                if hasattr(v, 'hour'):
                    out[k] = v.strftime('%Y-%d-%m, %I:%M:%S')
                elif v:
                    out[k] = v
        return out

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

    def publish(self, path_or_id, asset_type):
        identifier = Cascade.create_identifier(self, path_or_id, asset_type)
        identifier = {
            "identifier": identifier
        }

        response = self.client.service.publish(self.login, identifier)
        return response

    def get_groups_for_user(self, username=None):
        if username is None:
            return {}
        try:
            user = Cascade.read(self, username, "user")
            allowed_groups = user.asset.user.groups
        except AttributeError:
            allowed_groups = ""

        return allowed_groups.split(";")

    def unpublish(self, path_or_id, asset_type):
        identifier = Cascade.create_identifier(self, path_or_id, asset_type)
        identifier = {
            "identifier": identifier,
            "unpublish": True
        }

        response = self.client.service.publish(self.login, identifier)
        return response

    def move(self, new_folder_path_or_id, old_path_or_id, asset_type):
        identifier = Cascade.create_identifier(self, old_path_or_id, asset_type)
        new_identifier = Cascade.create_identifier(self, new_folder_path_or_id, "folder")

        moveParameters = {
            "destinationContainerIdentifier": new_identifier,
            "doWorkflow": False,
            "newName": None, ##can add newname here
        }

        response = self.client.service.move(self.login, identifier, moveParameters)
        return response

    def rename(self, path_or_id, new_name, asset_type):
        identifier = Cascade.create_identifier(self, path_or_id, asset_type)

        renameParameters = {
            "doWorkflow": False,
            "newName": new_name
        }

        # Note: rename is the same call as move, with different parameters
        response = self.client.service.move(self.login, identifier, renameParameters)
        return response

    def is_in_workflow(self, path_or_id, asset_type):
        identifier = Cascade.create_identifier(self, path_or_id, asset_type)

        response = self.client.service.readWorkflowInformation(self.login, identifier)

        if response.workflow is not None:
            if str(response.workflow.currentStep) != "finish":
                return True

        return False

