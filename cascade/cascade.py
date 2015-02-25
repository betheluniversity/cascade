

class Cascade(object):

    def __init__(self, service):
        from assets import asset
        self.service = service
        self.asset = asset.Asset(service)

    def get_service(self):
        return self.service

    def get_asset(self, asset_type, id_path, site_name=None):
        return self.asset.get_asset(asset_type, id_path, site_name)
