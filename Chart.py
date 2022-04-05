import numpy as np
import matplotlib.pyplot as plt

class Chart():

    def __init__(self):
        pass



    def drawLineChart(x,y,title,xlabel,ylabel):
        fig = plt.figure()
        plt.title(title)
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)

        plt.plot(x,y, marker='o')
        plt.show()
        pass

    def drawBarChart(x,y,title,xlabel,ylabel):
        #fig = plt.figure()
    
        plt.bar(x,y, align = 'center')
        #plt.xticks(x,y)
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)
        plt.title(title)
        plt.show()
        pass