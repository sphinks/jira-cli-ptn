'''
Created on 20.06.2011

@author: sphinks
'''

class SimpleCommand:
    '''
    Represents just simple command as objects with string name of command
    '''
    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        
    def get_name(self):
        return self.name