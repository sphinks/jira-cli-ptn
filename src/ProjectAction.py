'''
Created on 16.06.2011

@author: sphinks
'''
import JiraClient, Command

class ProjectAction:
    '''
    Actions for command project
    '''        
    def __call__(self, parser, namespace, values, option_string=None):
        print '%s:%s' % (namespace.login, namespace.password)
        jira_client = JiraClient.JiraClient("http://sandbox.onjira.com", namespace.login, namespace.password)
        #Debug call of one method without selection of action and without checking of login and password that was passed to JiraCli in line upper
        jira_client.getProjects()
    
    def perform_action(self, jira_client, cmd, option_string = None):
        if cmd == Command.Command.all_projects.get_name() and option_string:
            jira_client.getProjects()
        if cmd == Command.Command.project_name.get_name():
            jira_client.getProject(option_string)
            