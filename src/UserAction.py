'''
Created on 21.06.2011

@author: sphinks
'''

import JiraClient

class UserAction:
    '''
    Class for perfiming actions on user command
    '''
    def perform_action(self, jira_client, cmd, option_string = None):
        if (option_string):
            jira_client.getUserInfo(option_string)
        