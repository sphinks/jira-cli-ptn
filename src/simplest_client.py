"""
    The simplest possible client to connect to the JIRA REST API.
 
    This example uses basic authentication not cookies for simplicity.
 
    This example uses the restkit REST library. Using urllib2 is
    possible but not the simplest way.
"""
 
# For Python 2.5 download and install simplejson
# For Python 2.6 change this to: import json
import simplejson as json
 
# Download and install http://pypi.python.org/simple/ssl
# Download and install restkit
from restkit import Resource, SimplePool, BasicAuth, request
 
def rest_test(server_base_url, user, password, issue_key):
    '''
    Use restkit to make a REST request to JIRA
    '''
    verbose = False
 
    # A pool of connections
    pool = SimplePool(keepalive=2)
 
    # This sends the user and password with the request.
    auth = BasicAuth(user, password)
 
    resource_name = "issue"
    complete_url = "%s/rest/api/latest/%s/%s" % (server_base_url, resource_name, issue_key)
    resource = Resource(complete_url, pool_instance=pool, filters=[auth])
 
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
    issue = json.loads(response.body_string())
 
    # Pretty-print the JSON
    if verbose:
        print json.dumps(issue, sort_keys=True, indent=4)
 
    # The properties of the issue include:
    # self, html, key, transitions, expand, fields
 
    print "Issue key: %s" % issue['key']
 
    fields = issue['fields']
    for field_name in fields:
        field_object = fields[field_name]
        print "Field %s = %s" % (field_name, field_object['type'])
        # The type of the value of a field depends on the type of the field
        if field_name in ["summary"]:
            print "  Value = %s" % field_object['value']
 
if __name__ == '__main__':
    user = 'sphinks'
    password = '654321'
    server_url = 'http://sandbox.onjira.com'
    issue_key = "TST-1"
 
    rest_test(server_url, user, password, issue_key)