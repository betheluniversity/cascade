
class Cache(object):
    
    DEBUG = False
    DUMP = False

    cache = []
    instance = None
    service = None

    def __init__(self, service):
        self.cache = {}
        self.instance = None
        self.service = service
    
    def clear_cache(self):
        self.cache = {}

    def retrieve_asset(self, child):
        child_id = child.get_id()
        if not self.cache[child_id]:
            self.cache[child_id] = child.get_asset(self.service)
        return self.cache[child_id]

    def get_instance(self, service):
        self.service = service

        if not self.instance:
            self.instance = Cache()

        return self.instance
    



