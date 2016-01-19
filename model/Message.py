from google.appengine.ext import ndb


class Message(ndb.Model):
    msg = ndb.StringProperty()

    def insert_msg(self):
        self.put()

    def delete_msg(self):
        self.key.delete()
