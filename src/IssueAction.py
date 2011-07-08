'''
Created on 21.06.2011

@author: sphinks
'''
import Command
from Action import Action

class IssueAction(Action):
    '''
    Actions for command issue
    '''
    
    def perform_action(self, jira_client, cmd, args):
        #print "%s %s %s" % (cmd, args,  args.__dict__[Command.Command.commands["watchers"].get_name()])
        #If we provide name of issue
        if Command.Command.issue_name.get_name() in args and args.__dict__[Command.Command.issue_name.get_name()] != None:
            for option in Command.Command.issue_options:
                if option in args and args.__dict__[option]:
                    jira_client.getIssue(args.__dict__[Command.Command.issue_name.get_name()], Command.Command.issue_options[option])
                else:
                    jira_client.getIssue(args.__dict__[Command.Command.issue_name.get_name()])
                
        