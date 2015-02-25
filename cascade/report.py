

from utilities.cache import Cache


class Report(object):
    DEBUG = False
    DUMP = False

    def __init__(self, cascade):
        self.cascade = cascade
        self.results = []
        self.clear_results()
        service = self.cascade.get_service()
        self.cache = Cache(service)
        self.cache.clear_cache()

    def clear_results(self):
        self.results = []
        return self