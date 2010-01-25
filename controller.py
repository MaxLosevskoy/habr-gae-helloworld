#!/usr/bin/env python
# encoding: utf-8
"""
controller.py
$Id$
Created by Roman Kirillov on 2010-01-25.
"""
import view
import model

import logging 

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

class LoggedInRequestHandler(webapp.RequestHandler):
    def currentVisitor(self):
        user = users.get_current_user()
    
        # we shouldn't check user, as /login and /stats specifies 
        # login:required in app.yaml
    
        q = model.Visitor.all()
        q.filter('user = ', user)
    
        qr = q.fetch(2)
    
        if len(qr) == 0:
            u = model.Visitor()
        elif len(qr) > 1:
            # something is horribly wrong here, it shouldn't happen
            # but it still could
            logging.error("Duplicating user %s in datastore" % user.nickname())
            raise Exception("Duplicating user %s in datastore" % user.nickname())
        else:
            u = qr[0]
    
        self.currentVisitor = u
        return u

class DefaultRequestHandler(webapp.RequestHandler): 
    '''
    Handles default requests - checks whether user is logged in; if it is - saves an information about
    his visit in the database.
    '''
    
    def get(self):
        user = users.get_current_user()
        
        page = None
        if not user:
            page = view.StartPage(self.request)
        else:
            page = view.WelcomePage(self.request)
        
        page.render(self.response.out)

class StatsRequestController(LoggedInRequestHandler): 
    def get(self):
        u = self.currentVisitor()
        page = view.StatsPage(self.request, u)
        
        page.render(self.response.out)
        
class LoginController(LoggedInRequestHandler): 
    '''
    We use this controller just for handling the login event
    '''
    def get(self):
        u = self.currentVisitor()
        
        u.hits = u.hits + 1
        u.put()
        
        self.redirect('/')
        