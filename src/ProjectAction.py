'''
Created on 16.06.2011

@author: sphinks
'''
import Command

class ProjectAction:
    '''
    Actions for command project
    '''            
    def perform_action(self, jira_client, cmd, option_string = None):
        if cmd == Command.Command.all_projects.get_name() and option_string:
            jira_client.getProjects()
        if cmd == Command.Command.project_name.get_name():
            jira_client.getProject(option_string)
            