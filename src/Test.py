import Cli, Command, argparse, struct, JiraClient

#args = Command.Command.parser.parse_args(['--issue','TST-1', '-h'])
args = Command.Command.parser.parse_args('--projects --login sphinks --password 654321'.split())
print args
jira_client = JiraClient.JiraClient("http://sandbox.onjira.com", args.login, args.password)
jira_client.getProjects()

#jira_client.getIssue(args.issue)

