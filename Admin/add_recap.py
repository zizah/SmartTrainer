import cgi
import json

import webapp2
from google.appengine.api import taskqueue
from google.appengine.api import users


class AddRecap(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if (user):
            # Add the task to the default queue.
            data = cgi.FieldStorage()
            date = data.getvalue('date')
            titre_plan = data.getvalue('titre_plan')
            titre_exo = data.getvalue('titre_exo')
            success = data.getvalue('success')

            params = {
                'date': date,
                'titre_plan': titre_plan,
                'titre_exo': titre_exo,
                'success': success,
                'user': user.email()
            }

            taskqueue.add(url='/taskqueues/task_recap', params=params)