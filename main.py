#!/usr/bin/env python

'''
$Id$
'''

import controller

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import users

def main():
  application = webapp.WSGIApplication([('/', controller.DefaultRequestHandler), 
                                ('/stats', controller.StatsRequestController),
                                ('/login', controller.LoginController)],
                                       debug=True)
  util.run_wsgi_app(application)


if __name__ == '__main__':
  main()
