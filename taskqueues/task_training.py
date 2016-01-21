import unicodedata
import webapp2
import json
from model.Exercice import Exercice
from model.PlanEntrainement import PlanEntrainement


class TaskTraining(webapp2.RequestHandler):
    def post(self):
        inputTitle = self.request.get('inputTitle')
        inputDescription = self.request.get('inputDescription')
        domain = self.request.get('domain')
        duree_plan = self.request.get('duree_plan')
        u_exercices = self.request.get('exercices')
        str_exercices = unicodedata.normalize('NFKD', u_exercices).encode('ascii','ignore')
        exercices = json.loads(str_exercices)

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