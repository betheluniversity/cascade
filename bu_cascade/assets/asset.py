__author__ = 'ejc84332'


class Asset(object):

    def __init__(self, ws_connector, identifier=None):
        self.ws = ws_connector
        self.identifier = identifier

    def set_identifier(self, identifier):
        self.identifier = identifier

    def read_asset(self, identifier=None):
        if identifier:
            self.set_identifier(identifier)
        return self.ws.read(identifier)
