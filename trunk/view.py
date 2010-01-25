#!/usr/bin/env python
# encoding: utf-8
"""
view.py
$Id$
Created by Roman Kirillov on 2010-01-25.
"""

import os
from google.appengine.api import users
from google.appengine.ext.webapp import template

class StartPage:
    def __init__(self, request):
        self.request = request
    
    def render(self, out):
        template_values = {
            'login_url' : users.create_login_url("/login")
        }
        
        path = os.path.join('templates/please_login.html')
        out.write(template.render(path, template_values))

class WelcomePage:
    def __init__(self, request):
        self.request = request
        self.user = users.get_current_user()

    def render(self, out):
        template_values = {
            'username' : self.user.nickname(),
            'logout_url' : users.create_logout_url('/')
        }

        path = os.path.join('templates/welcome.html')
        out.write(template.render(path, template_values))
        
class StatsPage:
    def __init__(self, request, visitor):
        self.request = request
        self.visitor = visitor

    def render(self, out):
        
        template_values = {
            'username' : self.visitor.user,
            'lastVisit' : self.visitor.lastVisit,
            'hits' : self.visitor.hits
        }

        path = os.path.join('templates/stats.html')
        out.write(template.render(path, template_values))    