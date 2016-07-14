from suds.client import Client
from suds.sudsobject import asdict
from suds.transport import TransportError
import copy

from BeautifulSoup import BeautifulStoneSoup
import cgi

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
        return self.build_asset_structure(response)

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
        asset = self.recursive_asdict(asset)
        return asset

    def HTMLEntitiesToUnicode(self, text):
        """Converts HTML entities to unicode.  For example '&amp;' becomes '&'."""
        text = unicode(BeautifulStoneSoup(text, convertEntities=BeautifulStoneSoup.ALL_ENTITIES))
        return text

    def unicodeToHTMLEntities(self, text):
        """Converts unicode to HTML entities.  For example '&' becomes '&amp;'."""
        text = cgi.escape(text).encode('ascii', 'xmlcharrefreplace')
        return text

    def recursive_asdict(self, d):
        from suds.sudsobject import asdict

        """Convert Suds object into serializable format."""
        out = {}
        if type(d) is not dict:
            d = asdict(d)

        for k, v in d.iteritems():
            if hasattr(v, '__keylist__'):
                out[k] = self.recursive_asdict(v)
            elif isinstance(v, list):
                out[k] = []
                for item in v:
                    if hasattr(item, '__keylist__'):
                        out[k].append(self.recursive_asdict(item))
                    else:
                        out[k].append(item)

            elif v:
                # if v is True or k in ['lastModifiedDate', 'createdDate', 'lastPublishedDate']:
                # print k, v
                try:
                    # out[k] = BeautifulStoneSoup(v)
                    out[k] = v.encode('ascii', 'xmlcharrefreplace')
                except:
                    out[k] = v
                # else:

                # uni = self.HTMLEntitiesToUnicode(v)
                # htmlent = self.unicodeToHTMLEntities(uni)
                # out[k] = htmlent

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

    def publish(self, path_or_id, asset_type, destination=''):
        identifier = Cascade.create_identifier(self, path_or_id, asset_type)
        identifier = {
            "identifier": identifier,
            'destinations': self.get_destinations_for_string(destination)
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

    def move(self, old_path_or_id, new_folder_path_or_id, asset_type):
        identifier = Cascade.create_identifier(self, old_path_or_id, asset_type)
        new_identifier = Cascade.create_identifier(self, new_folder_path_or_id, "folder")

        moveParameters = {
            "destinationContainerIdentifier": new_identifier,
            "doWorkflow": False,
            "newName": None, # can add newname here
        }

        response = self.client.service.move(self.login, identifier, moveParameters)
        return response

    def copy(self, old_path_or_id, asset_type, destination_path_or_id, new_name):
        old_identifier = Cascade.create_identifier(self, old_path_or_id, asset_type)
        destination = Cascade.create_identifier(self, destination_path_or_id, 'folder')

        copyParameters = {
            "destinationContainerIdentifier": destination,
            "doWorkflow": False,
            "newName": new_name
        }

        response = self.client.service.copy(self.login, old_identifier, copyParameters)
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

    # can only be pages and blocks
    def load_base_asset_by_id(self, id, asset_type):
        asset = self.read(id, asset_type)
        if asset_type == 'page':
            asset_specific_key = 'page'
        elif asset_type == 'block':
            asset_specific_key = 'xhtmlDataDefinitionBlock'
        else:
            return None

        # Copy the base asset
        new_asset = self.build_asset_structure(copy.deepcopy(asset)['asset'])

        # reset path's and id's
        new_asset[asset_specific_key]['id'] = None
        new_asset[asset_specific_key]['parentFolderId'] = None
        new_asset[asset_specific_key]['parentFolderPath'] = None
        new_asset[asset_specific_key]['path'] = None

        # add in these keys manually to make sure they are in the asset
        new_asset[asset_specific_key]['metadata']['author'] = None
        new_asset[asset_specific_key]['metadata']['metaDescription'] = None

        # return asset parts based upon page/block/etc.
        new_asset_md = new_asset[asset_specific_key]['metadata']
        new_asset_sd = new_asset[asset_specific_key]['structuredData']

        return new_asset, new_asset_md, new_asset_sd

    def get_destinations_for_string(self, destination):
        if destination == 'staging.bethel.edu' or destination == 'staging':
            id = 'ba1381d58c586513100ee2a78fc41899'
            identifier = {'assetIdentifier': {
                'id': id,
                'type': 'destination',
            }
            }
            return identifier
        else:
            return ''