'''
Created on 24-Oct-2012

@author: koolkid
'''
from PIL import Image
class SimpleTransforms(object):
    '''
    Perform simple transforms and return the new transformed matrix
    '''
    def __init__(self):
        '''
        Empty Constructor
        '''
    
    '''
    Parameters to all the functions are arrays and the values returned 
    are transformed arrays corresponding to the transformation applied
    '''
    
    IDENTITY = "Identity"
    REFLECTION = "Reflection"
    FLIP = "Flip"
    ROTATION90 = "Rotation90"
    ROTATION180 = 'Rotation180'
    ROTATION270 = "Rotation270"
    
    @staticmethod
    def identity(image):
        return image
    
    @staticmethod
    def reflection(image):
        return image.transpose(Image.FLIP_LEFT_RIGHT)
    
    @staticmethod
    def flip(image):
        return image.transpose(Image.FLIP_TOP_BOTTOM)
    
    @staticmethod
    def rotation90(image):
        return image.rotate(90)
    
    @staticmethod
    def rotation180(image):
        return image.rotate(180)
    
    @staticmethod
    def rotation270(image):
        return image.rotate(270)
    
    @staticmethod
    def performTransform(image, transform):
        if transform == SimpleTransforms.IDENTITY:
            return SimpleTransforms.identity(image)
        elif transform == SimpleTransforms.FLIP:
            return SimpleTransforms.flip(image)
        elif transform == SimpleTransforms.REFLECTION:
            return SimpleTransforms.reflection(image)
        elif transform == SimpleTransforms.ROTATION90:
            return SimpleTransforms.rotation90(image)
        elif transform == SimpleTransforms.ROTATION180:
            return SimpleTransforms.rotation180(image)
        elif transform == SimpleTransforms.ROTATION270:
            return SimpleTransforms.rotation270(image)
        else:
            return None