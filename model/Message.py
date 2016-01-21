from google.appengine.ext import ndb


class Message(ndb.Model):
    msg = ndb.StringProperty()
    id_message = ndb.StringProperty()

    @staticmethod
    def getByIdMessage(id_message):
        res = Message.query(Message.id_message == id_message).fetch()
        if not res:
            return None
        else:
            return res



