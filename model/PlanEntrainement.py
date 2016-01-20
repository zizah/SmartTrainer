from google.appengine.ext import ndb
from model.Exercice import Exercice


class PlanEntrainement(ndb.Model):
    title = ndb.StringProperty()
    description = ndb.StringProperty()
    domain = ndb.StringProperty()
    duree = ndb.IntegerProperty()



