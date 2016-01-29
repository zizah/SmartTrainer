import webapp2
from google.appengine.api import users
import cgi
import globales
import json
from model.PlanEntrainement import PlanEntrainement
from model.Exercice import Exercice


class Details(webapp2.RequestHandler):
    def get(self):
        data = cgi.FieldStorage().getvalue('data')
        user = users.get_current_user()
        if user:
            url = users.create_logout_url('/')
            if data:
                data = json.load(data)
                plan = PlanEntrainement.get_by_id(data.get('id'))
                exercices = Exercice.get_exercices_from_ancestor(plan)
                self.response.write(globales.result_detail.render(user=user, url=url, plan=plan.title,exercices=exercices))
            else:
                self.response.write(globales.search.render(user=None, url=url))
        else:
            url = users.create_login_url('/')
            self.response.write(globales.search.render(user=None, url=url))
