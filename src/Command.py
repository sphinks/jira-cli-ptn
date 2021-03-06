'''
Created on 08.06.2011

@author: sphinks
'''
import argparse, ProjectAction, SimpleCommand, IssueAction, UserAction

class Command:
    '''
    Represents command of cli
    '''
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-l', '--login', help='Login', required=False)
    parser.add_argument('--password', help='Password', required=False)
    
    parser.add_argument('--auth', help='Flag that indicates to save current login and password into the file. In next you can work without entering --login and --password option.', required=False, action='store_true')
    
    subparser = parser.add_subparsers()
    
    
    issue_sparser = subparser.add_parser('issue', help='Working with issue')
    issue_sparser.add_argument('issue_name', help='Getting info about particular issue')
    issue_sparser.add_argument('-w', '--watchers',help='Get info about watching', required=False, action='store_true')
    
    projects_sparser = subparser.add_parser('projects', help='Working with project')
    projects_sparser.add_argument('--pname', help='Getting info about particular project', required=False)
    projects_sparser.add_argument('-a', '--all', help='Getting info about all projects', required=False, action='store_true')
    
    user_sparser = subparser.add_parser('user', help='Working with user')
    user_sparser.add_argument('user_name', help='Getting info about particular user')
    #all_projects = projects_sparser.add_argument('-a','-all_projects', help='Show all_projects available projects', action='store_true')
    
    #projects_command = parser.add_argument('-p','--projects', help='Command to show list of projects', action=ProjectAction.ProjectAction, nargs=0)
    #issue_command = parser.add_argument('-i', '--issue', help='Issue command that affords to get/set fields of issue')
    
    issue_name = SimpleCommand.SimpleCommand("issue_name")
    issue_watchers = SimpleCommand.SimpleCommand("watchers")
    login = SimpleCommand.SimpleCommand("login")
    password = SimpleCommand.SimpleCommand("password")
    all_projects = SimpleCommand.SimpleCommand("all")
    project_name = SimpleCommand.SimpleCommand("pname")
    user_name = SimpleCommand.SimpleCommand("user_name")
    
    commands = {
                issue_name.get_name(): issue_name,
                login.get_name(): login,
                password.get_name(): password,
                all_projects.get_name(): all_projects,
                project_name.get_name(): project_name,
                user_name.get_name(): user_name,
                issue_watchers.get_name(): issue_watchers
                }
    '''Here should be only commands that are main in branch of commands
    E.g. obligatory command issue_name and option command issue_watchers
    If we add both that when parce command line we will enter into the same action twice,
    but should enter only one time with issue_name and option -w
    '''
    actions = {
               all_projects.get_name():ProjectAction.ProjectAction(),
               project_name.get_name():ProjectAction.ProjectAction(),
               issue_name.get_name():IssueAction.IssueAction(),
               user_name.get_name():UserAction.UserAction(),
               issue_watchers.get_name():IssueAction.IssueAction()
               }
    issue_options = {
                     issue_watchers.get_name():"watchers",
                     }
    projects_options = {
                        project_name.get_name(): "pname",
                        all_projects.get_name(): "all",
                        
                        }

    def __init__(self):
        '''
        Constructor
        '''      
        