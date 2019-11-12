import numpy as np

class ArrayBase:
    '''ArrayBase class,parent of Animal and Landscape classes.







    '''
    def _init_(self, landscape):
        '''
        class constructor

        create any array of ints defining the landscape
        '''
        self.landscape = landscape
        self.landscape_X = landscape.shape[1]
        self.landscape_Y = landscape.shape[0]


    def getBaseArray(self):
        '''
        '''
        return self.baseArray

    def setBaseArray(self, newBaseArray):
        '''
        '''
        self.baseArray = newBaseArray

    def calDiffusionArray(self):
        '''
        This module is use to return the diffusion array for the basic change of arraybase
        '''
        raise NotImplementedError


