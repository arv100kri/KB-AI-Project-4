'''
Created on 24-Oct-2012

@author: Arvind Krishnaa Jagannathan
'''
import scipy
import numpy
from scipy.signal.signaltools import correlate2d as c2d

class SimpleMathUtils(object):
    '''
    Simple math utility functions 
    '''
    def __init__(self):
        '''
        Empty Constructor
        '''
        
    @staticmethod
    def selfCorrelation(imageArray):    #imageArray is the resut of Image.open()
        image = scipy.inner(numpy.asarray(imageArray), [299, 587, 114]) / 1000.0
        image = (image - image.mean())/ image.std()
        selfcorelationimageWithimage = c2d(image, image, mode = 'same')
        return selfcorelationimageWithimage.max()
    
    @staticmethod
    def corelationImage1Image2(imageArray1, imageArray2):
        image1 = scipy.inner(numpy.asarray(imageArray1), [299, 587, 114]) / 1000.0
        image2 = scipy.inner(numpy.asarray(imageArray2), [299, 587, 114]) / 1000.0
        
        image1 = (image1 - image1.mean())/ image1.std()
        image2 = (image2 - image2.mean())/ image2.std()
        
        corelationimage1Withimage2 = c2d(image1, image2, mode = 'same')
        return corelationimage1Withimage2.max()
    
    @staticmethod
    def findSumArrays(listofArrays):
        totalsum = 0
        for array in listofArrays:
            for element in array:
                totalsum+=element
        return totalsum