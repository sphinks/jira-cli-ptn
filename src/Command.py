'''
Created on 08.06.2011

@author: sphinks
'''
import argparse

class Command:
    '''
    Represents command of cli
    '''
    parser = argparse.ArgumentParser()
    issue_command = parser.add_argument('--issue', help='Issue command that affords to get/set fields of issue')
    login_command = parser.add_argument('--login', help='Login')
    password_command = parser.add_argument('--password', help='Password')
    projects_command = parser.add_argument('--projects', help='Command to show list of projects', action='store_true')
    commands = {"issue":issue_command, "login":login_command, "projects":projects_command, "password":password_command}

    def __init__(self):
        '''
        Constructor
        '''        
        