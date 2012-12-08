'''
Created on 22-Oct-2012

@author: koolkid
'''
import os
import math
class FileDirectory(object):
    '''
    classdocs
    '''

    __path = "Representations/"
    def __init__(self, i):
        '''
        Constructor
        '''
        self.__path+=str(i)
    
    def getDimensions(self):
        listing = os.listdir(self.__path)
        size = 0
        if len(listing)!=0:
            newPath = self.__path+"/Reference"
            listing = os.listdir(newPath)
            size = math.sqrt(len(listing))
                   
        return int(size)
    
    def getSizeOfPath(self):
        return len(os.listdir(self.__path))
    
    def setPath(self, path):
        self.__path = path