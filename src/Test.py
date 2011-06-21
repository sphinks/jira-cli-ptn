import Command, JiraClient


       

#args = Command.Command.parser.parse_args(['--issue','TST-1', '-h'])
#test_command = Command.Command.parser.add_argument('--test', action=TestAction.TestAction, nargs=1)
#args = Command.Command.parser.parse_args('projects -a'.split())
args = Command.Command.parser.parse_args('--login sphinks --password 654321 issue TST-1'.split())
#Debug show of all args
print args
print '---------------------------------------'
for cmd in Command.Command.actions:
    #print cmd
    #print Command.Command.commands[cmd].get_name()
    if cmd in args and args.__dict__[cmd] != None:
        #print '%s:%s' % (cmd, args.__dict__[cmd])
        jira_client = JiraClient.JiraClient("http://sandbox.onjira.com", args.login, args.password)
        Command.Command.actions[cmd].perform_action(jira_client, cmd, args.__dict__[cmd])


#Debug call of one method without selection of action and without checking of login and password that was passed to JiraCli in line upper
#jira_client.getProjects()


#jira_client.getIssue(args.issue_name)

