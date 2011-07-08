'''
Created on 14.06.2011

@author: sphinks
'''
import simplejson as json
from restkit import Resource, SimplePool, BasicAuth, request
import Command

class JiraClient:
    '''
    Class that represents client logic for JIRA
    '''

    def __init__(self, base_url, login, password):
        '''
        Constructor
        '''
        self.base_url = base_url
        self.login = login
        self.password = password
        self.verbose = False
 
        # A pool of connections
        self.pool = SimplePool(keepalive=2)
        
        # This sends the user and password with the request.
        self.auth = BasicAuth(login, password)
        
    def __make_request(self, resource):
        '''
        private method for making http request to jira api
        '''
        try:
            response = resource.get(headers = {'Content-Type' : 'application/json'})
        except Exception,ex:
            # ex.msg is a string that looks like a dictionary
            print "EXCEPTION: %s " % ex.msg
            return
        
        # Most successful responses have an HTTP 200 status
        if response.status_int != 200:
            print "ERROR: status %s" % response.status_int
            return
        
        # Convert the text in the reply into a Python dictionary
        result = json.loads(response.body_string())
        
        # Pretty-print the JSON
        if self.verbose:
            print json.dumps(result, sort_keys=True, indent=4)
        return result
    
    def __output_all_fields(self, fields):
        '''Common function to output fields in response from server'''
        '''for field_name in fields:
            field_object = fields[field_name]
            print "Field %s = %s" % (field_name, field_object['type'])
            # The type of the value of a field depends on the type of the field
            if field_name in ["summary"]:
                print "  Value = %s" % field_object['value']'''
        if fields != None:
            for field_name in fields:
                print "Field %s = %s" % (field_name, fields[field_name])
    
    def getIssue(self, issue_name, f_name=None):
        '''
        Method for getting issue fields
        '''
        resource_name = "issue"
        if f_name != None:
            complete_url = "%s/rest/api/latest/%s/%s/%s" % (self.base_url, resource_name, issue_name, f_name)
        else:
            complete_url = "%s/rest/api/latest/%s/%s" % (self.base_url, resource_name, issue_name)
        resource = Resource(complete_url, pool_instance=self.pool, filters=[self.auth])
       
        issue = self.__make_request(resource)
        
        # The properties of the project include:
        # self, html, key, transitions, expand, fields
        print "Issue key: %s" % issue_name
        
        if f_name == None:
            self.__output_all_fields(issue['fields'])
        else:
            if f_name == Command.Command.issue_watchers.get_name():
                self.__output_all_fields(issue)
                    
                
    def getProjects(self):
        '''
        Method for getting all projects
        '''
        resource_name = "project"
        complete_url = "%s/rest/api/latest/%s" % (self.base_url, resource_name)
        resource = Resource(complete_url, pool_instance=self.pool, filters=[self.auth])
       
        projects = self.__make_request(resource)
                
        for project_object in projects:
            print "Project %s = %s" % (project_object['name'], project_object['key'])
            
    def getProject(self, project_name, f_name = None):
        '''
        Method for getting particular projects        
        '''
        resource_name = "project"
        if (project_name):
            complete_url = "%s/rest/api/latest/%s/%s" % (self.base_url, resource_name, project_name)
            resource = Resource(complete_url, pool_instance=self.pool, filters=[self.auth])
       
            project = self.__make_request(resource)
            
            '''print "Project key: %s" % project['key']
            for field_object in project:
                print "Field %s = %s" % (field_object, project[field_object])'''
            self.__output_all_fields(project)
                
    
    def getUserInfo(self, user_name):
        '''
        Method for getting particular user        
        '''
        resource_name = "user"
        if (user_name):
            complete_url = "%s/rest/api/latest/%s?username=%s" % (self.base_url, resource_name, user_name)
            resource = Resource(complete_url, pool_instance=self.pool, filters=[self.auth])
       
            user = self.__make_request(resource)
            #print user
            #print "Project key: %s" % user['key']
            '''for field_object in user:
                print "Field %s = %s" % (field_object, user[field_object])'''
            self.__output_all_fields(user)