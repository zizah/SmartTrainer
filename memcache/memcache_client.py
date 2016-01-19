import cgi

from google.appengine.api import memcache
import webapp2


class MemCacheClient(webapp2.RedirectHandler):
    def get(self, *args, **kwargs):
        pass

    @staticmethod
    def add_data(key, value):
        memcache.add(key, value)

    @staticmethod
    def add_multi_data(values):
        memcache.add_multi(values)

    @staticmethod
    def get_data(key):
        return memcache.get(key)