import webapp2
import globales
from memcache.memcache_client import MemCacheClient


class Logout(webapp2.RequestHandler):
    def post(self):
        self.response.delete_cookie('ACSID')
        self.response.delete_cookie('__utma')
        self.response.delete_cookie('__utmz')
        self.response.write(globales.search.render(user=None))
