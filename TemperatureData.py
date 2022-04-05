from Date import *

class TemperatureData():
   
    #Calls from FileIO 
    def __init__(self,mo,ye,mint,maxt,sf):
        self.mo = mo 
        self.ye = ye
        self.Date = Date(ye,mo)
        self.mint = mint
        self.maxt = maxt
        self.sf = sf

    #Calls from Date, gives months and year a variable
    #def date(self):
    '''
        mo = Date.getMonths()
        ye = Date.getYears()

    #creates an array for all minimum temperature, [:[3]] takes all values from
    #3rd index, .flatten() creates the array
    def minTemperature(self):
         mint = self.weadata[:,[3]].flatten()
         #print(mint)
         return mint
    
    #creates an array for all max temperature, [:[2]] takes all values from
    #2nd index, .flatten() creates the array
    def maxTemperature(self):
        maxt = self.weadata[:,[2]].flatten()
        #print(maxt)
        return maxt

    #creates an array for all snowfall, [:[4]] takes all values from
    #4th index, .flatten() creates the array
    def snowFall(self):
        sf = self.weadata[:,[4]].flatten()
        #print(sf)
        return sf
    '''