'''
Created on 08.07.2011

@author: sphinks
'''
import abc


class Action:
    '''
    Base class for all actions
    '''
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def perform_action(self, jira_client, cmd, args):
        '''
        Function for perfoming action
        '''
        