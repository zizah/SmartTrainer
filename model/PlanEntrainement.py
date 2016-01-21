from google.appengine.ext import ndb
from model.Exercice import Exercice

class PlanEntrainement(ndb.Model):
    user = ndb.StringProperty()
    title = ndb.StringProperty()
    description = ndb.StringProperty()
    domain = ndb.StringProperty()
    duree = ndb.IntegerProperty()

    @staticmethod
    def get_all_domain_by_user(user):
        res = PlanEntrainement.query(user=user).order(PlanEntrainement.domain).fetch()
        if not res:
            return []
        else:
            return res



