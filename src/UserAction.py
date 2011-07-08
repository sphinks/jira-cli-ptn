'''
Created on 21.06.2011

@author: sphinks
'''

import Command 
from Action import Action

class UserAction(Action):
    '''
    Class for perfiming actions on user command
    '''
    def perform_action(self, jira_client, cmd, args):
        if (args.__dict__[Command.Command.user_name.get_name()]):
            jira_client.getUserInfo(args.__dict__[Command.Command.user_name.get_name()])
        