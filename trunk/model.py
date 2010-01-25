#!/usr/bin/env python
# encoding: utf-8
"""
model.py
$Id$
Created by Roman Kirillov on 2010-01-25.
"""

import datetime
from google.appengine.ext import db
from google.appengine.api import users


class Visitor(db.Model):
    '''
    Simple object which uses Google DataStore persistence model
    '''
    
    '''UserProperty encapsulates information about a Google's 
    user account available to application. It is set to
    use current user as a default user automatically
    whever new object is created'''
    user = db.UserProperty(required = True, auto_current_user_add = True) 
    
    '''DateTimeProperty uses standard underlying datetime.datetime
    and is set to auto-update to now() whenever record is saved'''
    lastVisit = db.DateTimeProperty(auto_now = True)
    
    '''Very simple integer property with default value of 0'''
    hits = db.IntegerProperty(default = 0)