from plone import api
from plone.dexterity.browser import add
from plone.memoize import ram
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

import datetime, time, json, uuid

class UserCheckView(BrowserView):

   
    def __call__(self):
        output = "."
        users = api.user.get_users()
        user = api.user.get(userid=self.request.get('netid','abcdefg')) #, username=None)

            
            
        return output
        
        
    @property
    def portal(self):
        return api.portal.get()
        
