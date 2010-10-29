collective.getpid Package Readme
================================

Overview
--------

GetPid of a zope process


Simply get the pid via http request
-----------------------------------
    >>> import collective.getpid
    >>> import Products.Five
    >>> from Products.Five.zcml import load_config
    
    >>> load_config('configure.zcml' ,  Products.Five)
    >>> load_config('test.zcml', collective.getpid)
    

    >>> t = self.app.restrictedTraverse('getPid')()

Buildout
--------

You have an example buildout under docs/buildout    
    
    



        
