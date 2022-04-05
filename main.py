import numpy as np
import matplotlib.pyplot as plt

from Date import *
from FileIO import * 
from TemperatureData import *
from WeatherAnalyzer import *
#from Chart import *
import os 
def main():
    file_name = "Project\CalgaryWeather.csv"
    fileio = FileIO(file_name)
    weadata = FileIO.readFromFile(fileio)
    months = weadata[:,[1]].flatten()
    years = weadata[:,[0]].flatten()
    mint = weadata[:,[3]].flatten()
    maxt = weadata[:,[2]].flatten()
    sf = weadata[:,[4]].flatten()
    day = Date(years,months)
    Temp = TemperatureData(months,years,mint,maxt,sf)
    WA = WeatherAnalyzer(Temp)

    #chart = Chart()

    user = True

    while user:
        print("1-Get Minimum Temperature of 1990-2019")
        print("2-Get Maximum Temperature of 1990-2019")
        print("3-Get Minimum Temperature of 1990-2019 Annually")
        print("4-Get Maximum Temperature of 1990-2019 Annually")
        print("5-Get Average Snowfall between 1990-2019 Annually")
        print("6-Get Average Temperature between 1990-2019 Annnually")
        print("7-Draw the line chart for minimum temperature of 1990-2019")
        print("8-Draw the line chart for maximum temperature of 1990-2019")
        print("9-Draw the bar chart for average temperature of 1990-2019")
        print("10-Draw the bar chart for average snowfall of 1990-2019")
        print("11-Exit")
        
        user = input('Enter an option ')

        if user == '1':
            print("\n 1-Get Minimum Temperature of 1990-2019")
            print("----------------------------------------------------------")
            WA.getMinTemp()

        elif user == '2':
            print("\n 2-Get Maximum Temperature of 1990-2019")
            print("----------------------------------------------------------")
            WA.getMaxTemp()

        elif user == '3':
            print("\n 3-Get Minimum Temperature of 1990-2019 Annually")
            print("----------------------------------------------------------")
            WA.getMinTempA()

        elif user == '4': 
            print("\n 4-Get Maximum Temperature of 1990-2019 Annually")
            print("----------------------------------------------------------")
            WA.getMaxTempA()
        
        elif user == '5':
            print("\n 5-Get Average Snowfall between 1990-2019 Annually")
            print("----------------------------------------------------------")
            WA.getAvgSnowFallAnnually()

        elif user == '6':
            print("\n 6-Get Average Temperature between 1990-2019 Annually")
            print("----------------------------------------------------------")
            WA.getAvgTempAnnually()
        elif user == '7':
            print("\n 7-Draw the line chart for minimum temperature of 1990-2019")
            print("----------------------------------------------------------")
            WA.createMinLineChart()
        elif user == '8':
            print("\n 8-Draw the line chart for maximum temperature of 1990-2019")
            print("----------------------------------------------------------")
            WA.createMaxLineChart()
        elif user == '9':
            print("\n 9-Draw the bar chart for average temperature of 1990-2019")
            print("----------------------------------------------------------")
            WA.createAvgTempBarChart()
        elif user == '10':
            print("\n 10-Draw the bar chart for average snowfall of 1990-2019")
            print("----------------------------------------------------------")
            WA.createAvgSnowBarChart()
        elif user == '11':
            print("\n 11- Exit")
            user = None
        
        else:
            print("\n Option not valid")
        



if __name__ == "__main__":
    main()


 