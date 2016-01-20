from google.appengine.ext import ndb


class Exercice(ndb.Model):
    titleDescription = ndb.StringProperty()
    exerciceDescription = ndb.StringProperty()
    duree = ndb.IntegerProperty()
    repetition = ndb.IntegerProperty()



