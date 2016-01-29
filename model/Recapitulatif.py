from google.appengine.ext import ndb


class Recapitulatif(ndb.Model):
    date = ndb.StringProperty()
    id_user = ndb.StringProperty()
    titre_plan = ndb.StringProperty()
    titre_exo = ndb.StringProperty()
    success = ndb.StringProperty()

    @staticmethod
    def get_recap_id(id_user):
        res = Recapitulatif.query(Recapitulatif.id_user == id_user).fetch()
        if not res:
            return []
        else:
            return res