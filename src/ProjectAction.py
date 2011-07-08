'''
Created on 16.06.2011

@author: sphinks
'''
import Command
from Action import Action

class ProjectAction(Action):
    '''
    Actions for command project
    '''            
    def perform_action(self, jira_client, cmd, args):
        if Command.Command.all_projects.get_name() in args and args.__dict__[Command.Command.all_projects.get_name()]:
            jira_client.getProjects()
        else:
            if Command.Command.project_name.get_name() in args and args.__dict__[Command.Command.project_name.get_name()] != None:
                for option in Command.Command.projects_options:
                    if option in args and args.__dict__[option]:
                        jira_client.getProject(args.__dict__[Command.Command.project_name.get_name()], Command.Command.projects_options[option])
                    else:
                        jira_client.getProject(args.__dict__[Command.Command.project_name.get_name()])
            '''if cmd == Command.Command.all_projects.get_name() and option_string:
                jira_client.getProjects()
            if cmd == Command.Command.project_name.get_name():
                jira_client.getProject(option_string)'''
            