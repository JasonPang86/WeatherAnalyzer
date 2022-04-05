from FileIO import *
from TemperatureData import *
from Date import *
import numpy as np
from Chart import *

class WeatherAnalyzer:
    
    


    def __init__(self, weadata):
        self.weadata = weadata

    def getMinTemp(self):
        print ('Minimum temperature of 1990-2019:', np.min(self.weadata.mint),"°C")

        return 

    def getMinTempA(self):
        j = 1990
        split = self.weadata.mint
        minTemps = []
        for i in range(0, 359, 12):
            plit = split[i:i + 12]
            chunk = (np.min(plit))
            minTemps.append(chunk)
            print ('Minimum Temperature of ',j,':', chunk,"°C")

            j += 1
        
        return minTemps  

    def getMaxTemp(self):
        print ('Maximum temperature of 1990-2019:', np.max(self.weadata.maxt),"°C")

        return

    def getMaxTempA(self):
        j = 1990
        maxTemps = []
        for i in range(0, 359,12):
            split = self.weadata.maxt
            plit = split[i:i + 12]
            chunk = (np.max(plit))
            maxTemps.append(chunk)
            print ('Maximum Temperature of ',j,':', chunk,"°C")

            j += 1

        return maxTemps
    
    def getAvgSnowFallAnnually(self):
        j = 1990
        avgSnow = []
        for i in range(0, 359,12):
            split = self.weadata.sf
            plit = split[i:i + 12]
            
            ft = np.mean(plit)

            avgSnow.append(ft)

            print ('Average Snowfall of ',j,':', round(ft,2),"cm")

            j += 1

        return avgSnow
    
    def getAvgTempAnnually(self):
        d = 1990
        avgTemps = []
        mon = []
        mit = self.weadata.mint
        mat = self.weadata.maxt
        
        for j in range(0,359,12):
            A = mit[j:j + 12]
            B = mat[j:j + 12]

            for i in range(len(A)):
                mon.append((A[i] + B[i])/2)

            split = mon[j:j + 12]
            ft = np.mean(split)
            avgTemps.append(ft)

            print('Average Temperature of ',d,':', round(ft,2),"°C",)

            d += 1       

        return avgTemps

        


    def createMinLineChart(self):
        years = []
        for year in range(1990,2020):
            years.append(year)
        Chart.drawLineChart(years,self.getMinTempA(),"Minimum temperatures of 1990-2019", "Years", "Temperature (°C)")

    def createMaxLineChart(self):
        years = []
        for year in range(1990,2020):
            years.append(year)
        Chart.drawLineChart(years,self.getMaxTempA(),"Maximum temperatures of 1990-2019", "Years", "Temperature (°C)")   

    def createAvgTempBarChart(self):
        years = []
        for year in range(1990,2020):
            years.append(year)
        Chart.drawBarChart(years,self.getAvgTempAnnually(),"Average temperatures of 1990-2019", "Years", "Temperature (°C)")

    def createAvgSnowBarChart(self):
        years = []
        for year in range(1990,2020):
            years.append(year)
        Chart.drawBarChart(years,self.getAvgSnowFallAnnually(),"Average snowfall of 1990-2019", "Years", "Snowfall (cm)")

    



