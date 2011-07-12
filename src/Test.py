import Command, JiraClient, ConfigFile, StdInOutWrapper

       

#args = Command.Command.parser.parse_args(['--issue','TST-1', '-h'])
#test_command = Command.Command.parser.add_argument('--test', action=TestAction.TestAction, nargs=1)
#args = Command.Command.parser.parse_args('projects -a'.split())
#args = Command.Command.parser.parse_args('--login sphinks --password 654321 --auth issue TST-1 -w'.split())
args = Command.Command.parser.parse_args('issue TST-1 -w'.split())
#Debug show of all args
print args
print '---------------------------------------'


auth = {"login":"",
        "password":""}

config = ConfigFile.ConfigFile()
if args.login == None and args.password == None:
    StdInOutWrapper.StdInOutWrapper.output("> No login and password specified. Looking for it in config file...")
    auth = config.readLoginPassword()
    if auth['login'] != "":
        StdInOutWrapper.StdInOutWrapper.output("> Success.")
        args.login = auth['login']
        args.password = auth['password']
    else:
        StdInOutWrapper.StdInOutWrapper.output("> Auth info cann`t be found.")
        args.login = StdInOutWrapper.StdInOutWrapper.getFromInput("> Enter your login: ")
        args.password = StdInOutWrapper.StdInOutWrapper.getFromInput("> Enter your password: ")
        if args.auth:
            StdInOutWrapper.StdInOutWrapper.output("> Set option --auth. Saving login and password to config file. Now you can skip entering login and password.")
            config.writeLoginPassword(args.login, args.password)
else:
    if args.login != None and args.password != None:
        if args.auth:
            StdInOutWrapper.StdInOutWrapper.output("> Set option --auth. Saving login and password to config file. Now you can skip entering login and password.")
            config.writeLoginPassword(args.login, args.password)
    else:
        if args.login != None:
            args.password = StdInOutWrapper.StdInOutWrapper.getFromInput("> Enter your password: ")
            if args.auth:
                StdInOutWrapper.StdInOutWrapper.output("> Set option --auth. Saving login and password to config file. Now you can skip entering login and password.")
                config.writeLoginPassword(args.login, args.password)
            


for cmd in Command.Command.actions:
    #print cmd    
    #print Command.Command.commands[cmd].get_name()
    if cmd in args and args.__dict__[cmd]:
        #print '%s:%s' % (cmd, args.__dict__[cmd])
        jira_client = JiraClient.JiraClient("http://sandbox.onjira.com", args.login, args.password)
        Command.Command.actions[cmd].perform_action(jira_client, cmd, args)
        break;

