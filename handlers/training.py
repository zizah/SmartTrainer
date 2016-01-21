import webapp2
from google.appengine.api import users

import globales


class Training(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url('/')
            self.response.write(globales.add_training.render(user=user, url=url))
        else:
            url = users.create_logout_url('/')
            self.response.write(globales.search.render(user=None, url=url))
