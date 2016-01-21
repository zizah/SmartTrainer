import webapp2
import cgi
from model.Message import Message

class AddMessage(webapp2.RequestHandler):
    def get(self):
        msg = cgi.escape(self.request.get('message_content'))

        message = Message()
        message.id_message = "welcome_message"
        message.msg = msg
        message.put()

