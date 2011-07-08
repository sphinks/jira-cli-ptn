'''
Created on 08.07.2011

@author: sphinks
'''
import ConfigParser

class ConfigFile():
    '''
    Class for config file
    '''
    def __init__(self):
        self.__config_name = "config.cfg"
        self.__config = ConfigParser.RawConfigParser()
        
    def __writeToConfig(self, section, field, value):
        '''
        Writing new values to config
        '''
        if not self.__config.has_section(section):
            self.__config.add_section(section)
        self.__config.set(section, field, value)
        
    def __wirteToFile(self):
        if self.__config != None:
            with open(self.__config_name, 'wb') as configfile:
                self.__config.write(configfile)
        
    def __readConfigFile(self):
        self.__config.read(self.__config_name)
        
    def __getFromConfig(self, section, field):
        return self.__config.get(section, field)
    
    def readLoginPassword(self):
        self.__readConfigFile()
        result = {
                  'login': self.__getFromConfig('Main', 'Login'),
                  'password': self.__getFromConfig('Main', 'Password'),
                  }
        return result
    
    def writeLoginPassword(self, login, password = None):
        self.__writeToConfig("Main", "Login", login)
        if password != None:
            self.__writeToConfig("Main", "Password", password)
        self.__wirteToFile()