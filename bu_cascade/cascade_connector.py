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

    def read(self, path_or_id, read_type="page"):

        if path_or_id[0] == "/":
            identifier = {
                'type': read_type,
                'path': {
                    'path': path_or_id,
                    'siteId': self.site_id
                }
            }
        else:
            identifier = {
                'id': path_or_id,
                'type': read_type,
            }

        response = self.client.service.read(self.login, identifier)
        return response



