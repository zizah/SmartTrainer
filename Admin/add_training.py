import cgi
import json
import pickle
from json import JSONEncoder

import webapp2
import globales
from google.appengine.api import users

from model.Exercice import Exercice
from model.PlanEntrainement import PlanEntrainement


class AddTraining(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if (user):
            data = cgi.FieldStorage()
            inputTitle = data.getvalue('inputTitle')
            inputDescription = data.getvalue('inputDescription')
            domain = data.getvalue('domain')
            duree_plan = data.getvalue('duree_plan')
            exercices = json.loads(data.getvalue('exercices'))

            plan = PlanEntrainement(
                    title=inputTitle,
                    description=inputDescription,
                    domain=domain,
                    duree=int(duree_plan))
            e_key = plan.put()

            for ex in exercices:
                exercice = Exercice(parent=e_key)
                exercice.titleDescription = str(ex.get('titleDescription').encode('utf-8'))
                exercice.exerciceDescription = str(ex.get('exerciceDescription').encode('utf-8'))
                exercice.duree = int(ex.get('duree'))
                exercice.repetition = int(ex.get('repetition'))
                exercice.put()
