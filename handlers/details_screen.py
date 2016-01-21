import webapp2
from google.appengine.api import users

import globales
from model.PlanEntrainement import PlanEntrainement


class Search(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url('/')
            self.response.write(globales.result_detail.render(user=user, url=url))
        else:
            url = users.create_login_url('/')
            self.response.write(globales.search.render(user=None, url=url))
