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
from google.appengine.api import users
import webapp2
from model.Message import Message
import globales
from Admin.welcome_message import AddMessage
from memcache.memcache_client import MemCacheClient
from google.appengine.api import memcache


class MainHandler(webapp2.RequestHandler):
    def get(self):
        msg = memcache.get('welcome_msg')
        if msg:
            print "exists bingo"
        else:
            print "not exist"
            welcome = Message()
            welcome_msg = welcome.get_by_id(5629499534213120)
            msg = str(welcome_msg.msg)
            memcache.add(key="welcome_msg", value=str(msg), time=3600)
        self.response.write(globales.index.render(msg=msg))
        self.response.write(globales.add_training.render())

        # Checks for active Google account session
        user = users.get_current_user()
        if user:
            self.response.write(globales.SEARCH.render(user=user))
        else:
           self.response.write(globales.SEARCH.render(user=None))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/Admin/welcome_message', AddMessage)
], debug=True)




