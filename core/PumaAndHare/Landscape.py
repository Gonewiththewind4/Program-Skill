from ArrayBase import *
import numpy as np

class Landscape(ArrayBase):
    '''
    '''
    def _init_(self, landscape):
        '''
        '''
        super()._init_(landscape)

        if np.sum(landscape) == 0:
            raise Exception("There is no Land for diffusion")
        self.baseArray = landscape
        self.diffusionArray = self.calDiffusionArray()


