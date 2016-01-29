from google.appengine.ext import ndb


class Exercice(ndb.Model):
    titleDescription = ndb.StringProperty()
    exerciceDescription = ndb.StringProperty()
    duree = ndb.IntegerProperty()
    repetition = ndb.IntegerProperty()

    @staticmethod
    def get_exercices_from_ancestor(ancestor):
        res = Exercice.query(ancestor=ancestor.key).fetch()
        if not res:
            return []
        else:
            return res




