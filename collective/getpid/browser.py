# -*- coding: utf-8 -*-
# Copyright (C) 2010 Alterway Solutions 

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; see the file COPYING. If not, write to the
# Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.



from zope.interface import implements
from zope.interface import Interface
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class IProcess(Interface):
    """ interface for Process """

class Process(BrowserView):
    """ see  IProcess """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def getPid(self):
        """ return  the pid of proccess"""
        return self.context.Control_Panel.process_id
             
     
