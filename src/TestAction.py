'''
Created on 16.06.2011

@author: sphinks
'''
import argparse

class TestAction(argparse.Action):
    '''
    Test action for parsed command
    ''' 
    def __call__(self, parser, namespace, values, option_string=None):
        print '%r, %r, %r' % (namespace, values, option_string)
        setattr(namespace, self.dest, values)
        