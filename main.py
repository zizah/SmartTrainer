#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from google.appengine.api import memcache
from google.appengine.api import users

import globales
from Admin.add_training import AddTraining
from Admin.welcome_message import AddMessage
from Admin.add_recap import AddRecap
from auth.logout import Logout
from handlers.details_screen import Details
from handlers.search import Search
from handlers.training import Training
from model.Message import Message
from taskqueues.task_training import TaskTraining
from taskqueues.task_recap import TaskRecap


class MainHandler(webapp2.RequestHandler):
    def get(self):
         msg = memcache.get('welcome_msg')
         if msg:
             print "exists bingo"
         else:
             print "not exist"
             welcome_msg = Message.getByIdMessage("welcome_message")
             if welcome_msg:
                msg = welcome_msg[0].msg
                memcache.add(key="welcome_msg", value=str(msg), time=3600)
         user = users.get_current_user()
         if user:
            self.response.write(globales.index.render(msg=msg, user=user))
         else:
             #self.redirect(users.create_login_url(self.request.uri))
             self.response.write(globales.index.render(msg=msg, user=None))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/Admin/welcome_message.*', AddMessage),
    ('/Admin/add_training.*', AddTraining),
    ('/Admin/add_recap.*', AddRecap),
    ('/handlers/training.*', Training),
    ('/handlers/search.*', Search),
    ('/handlers/details_screen.*', Details),
    ('/taskqueues/task_training.*', TaskTraining),
    ('/taskqueues/task_recap.*', TaskRecap),
    ('/auth/logout', Logout)
], debug=True)
