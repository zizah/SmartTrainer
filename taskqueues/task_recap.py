import webapp2

from model.Recapitulatif import Recapitulatif


class TaskRecap(webapp2.RequestHandler):
    def post(self):
        email = self.request.get('user')
        date = self.request.get('date')
        titre_plan = self.request.get('titre_plan')
        titre_exo = self.request.get('titre_exo')
        success = self.request.get('success')

        recap = Recapitulatif(
                id_user=str(email),
                date=str(date),
                titre_plan=str(titre_plan),
                titre_exo=str(titre_exo),
                success=str(success))
        recap.put()
