import numpy as np

class FileIO():

    def __init__(self, file_name):
        self.file_name = file_name

    def readFromFile(self):
        wea = np.genfromtxt(self.file_name, delimiter = ',', dtype = np.float, skip_header= 1) 
        #np.genfromtext reads and stores data in memory, in "wea" delimiter splits the data using commas, 
        # dtype converts all the values to floats, skip headliner skips the headliner xd

        return wea


    
    
    
