'''
Created on 21.06.2011

@author: sphinks
'''
import Command, JiraClient

class IssueAction:
    '''
    Actions for command issue
    '''
    def perform_action(self, jira_client, cmd, option_string = None):
        if option_string:
            jira_client.getIssue(option_string)
        