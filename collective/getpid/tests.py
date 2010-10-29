import unittest
import collective.getpid
from zope.testing import doctestunit
from zope.component import testing
from Testing import ZopeTestCase as ztc


def setup(test):
    ztc.installPackage(collective.getpid)
    

    
    
def test_suite():
    return unittest.TestSuite([

        # Unit tests for your API
        #doctestunit.DocFileSuite(
        #    'README.txt', package='collective.getpid',
        #    setUp=testing.setUp, tearDown=testing.tearDown),

        #doctestunit.DocTestSuite(
        #    module='collective.getpid.mymodule',
        #    setUp=testing.setUp, tearDown=testing.tearDown),

        # Integration tests that use ZopeTestCase

        
        #ztc.ZopeDocFileSuite(
        #    'README.txt', package='collective.getpid',
        #    setUp=setup, tearDown=testing.tearDown),

        ztc.FunctionalDocFileSuite(
            'README.txt', package='collective.getpid'),

        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
