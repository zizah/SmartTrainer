import webapp2
from google.appengine.api import users

import globales
from model.PlanEntrainement import PlanEntrainement


class Search(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url('/')
            domains = PlanEntrainement.get_all_domain_by_user(str(user.email()))
            self.response.write(globales.search.render(user=user, domains=domains, url=url))
        else:
            url = users.create_login_url('/')
            self.response.write(globales.search.render(user=None, url=url))
