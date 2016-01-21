import cgi
import json

import webapp2
from google.appengine.api import taskqueue
from google.appengine.api import users


class AddTraining(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if (user):
            # Add the task to the default queue.
            data = cgi.FieldStorage()
            inputTitle = data.getvalue('inputTitle')
            inputDescription = data.getvalue('inputDescription')
            domain = data.getvalue('domain')
            duree_plan = data.getvalue('duree_plan')
            exercices = data.getvalue('exercices')

            params = {
                'inputTitle': inputTitle,
                'inputDescription': inputDescription,
                'domain': domain,
                'duree_plan': duree_plan,
                'exercices': exercices
            }

            taskqueue.add(url='/taskqueues/task_training', params=params)




