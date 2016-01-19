import webapp2
import cgi
from model.Message import Message

class AddMessage(webapp2.RequestHandler):
    def get(self):
        msg = cgi.escape(self.request.get('message_content'))

        message = Message()
        message.msg = msg
        message.insert_msg()

