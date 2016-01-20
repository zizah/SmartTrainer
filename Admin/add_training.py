import cgi
import json
import pickle
from json import JSONEncoder

import webapp2

from model.Exercice import Exercice
from model.PlanEntrainement import PlanEntrainement


class AddTraining(webapp2.RequestHandler):
    def get(self):
        data = cgi.FieldStorage()
        inputTitle = data.getvalue('inputTitle')
        inputDescription = data.getvalue('inputDescription')
        domain = data.getvalue('domain')
        duree_plan = data.getvalue('duree_plan')
        exercices = data.getvalue('exercices')

        plan = PlanEntrainement()
        plan.title = inputTitle
        plan.description = inputDescription
        plan.domain = domain
        plan.duree = int(duree_plan)
        plan.put()

        for ex in exercices:
            exercice = Exercice(parent=plan)
            exercice.titleDescription = ex.get('titleDescription')
            exercice.exerciceDescription = ex.get('exerciceDescription')
            exercice.duree = int(ex.get('duree'))
            exercice.repetition = int(ex.get('repetition'))
            exercice.put()