import cgi
import json
import pickle
from json import JSONEncoder

import webapp2
import globales
from google.appengine.api import users


class Training(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        self.response.write(globales.add_training.render(user=user))