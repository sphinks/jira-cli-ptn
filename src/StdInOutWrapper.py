'''
Created on 10.07.2011

@author: sphinks
'''

class StdInOutWrapper():
    '''
    Wrapper for using stdin and stdout
    '''
    
    @staticmethod
    def output(message):
        print message
    @staticmethod    
    def getFromInput(comment = ""):
        return raw_input(comment)
            
