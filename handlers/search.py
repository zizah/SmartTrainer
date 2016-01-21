import cgi
import json
import pickle
from json import JSONEncoder

import webapp2
import globales
from google.appengine.api import users
from model.PlanEntrainement import PlanEntrainement


class search(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            domains = PlanEntrainement.get_all_domain_by_user(str(user.email()))
            self.response.write(globales.add_training.render(user=user, domains=domains))
        else:
            self.response.write(globales.search.render(user=None))
