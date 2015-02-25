__author__ = 'ejc84332'

from . import t

class Asset(object):

    def __init__(self, service, idenifier=None):
        self.service = service
        self.identifier = idenifier
        self.types = T()

    def set_identifier(self, identifier):
        self.identifier = identifier

    def get_asset(self, asset_type, id_path=None, site_name=None):

        if id_path:
            self.set_identifier(id_path)

        if asset_type not in T.get_type_array():
            raise NoSuchTypeException("The type $type does not exist.")

        class_name = self.types.type_class_name_map[asset_type]

        try:
            return class_name(self.service, self.service.create_id(asset_type, id_path, site_name))
        except:
            pass
            # if(self.DEBUG):
            #     { DebugUtility::out( $e->getMessage() ); }
            # throw $e;
