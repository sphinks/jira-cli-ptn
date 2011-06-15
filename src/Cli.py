'''
Created on 08.06.2011

@author: sphinks
'''
import argparse

class Cli:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')
        parser.add_argument('--sum', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='sum the integers (default: find the max)')

        args = parser.parse_args()
        print args.accumulate(args.integers)
        