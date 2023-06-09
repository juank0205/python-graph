import numpy as np
import math
class Function(object):
    def __init__(self, string:str) -> None:
        self.string = string
        self.__isDigit = self.string.isdigit()

    def set_string(self, string):
        self.string = string
        self.__isDigit = self.string.isdigit()

    #Getters
    def get_isDigit(self) -> bool:
        return(self.__isDigit)

    def evalFunction(self, xArray) -> tuple:
        try:
            yArray = eval(self.string, {'x': xArray, 'np': np, 'math': math} ) if not(self.__isDigit) else [float(self.string)]*len(xArray)
            return (xArray, yArray)
        except:
            raise Exception("Not valid")
        

class differentialEquation(Function):
    def __init__(self, string: str, initialPoint: tuple) -> None:
        super().__init__(string) 
        self.initialPoint = initialPoint
        self.__step = 0.1 
        self.__isDigit = True

    def get_initial_x(self):
        return self.initialPoint[0]

    def get_initial_y(self):
        return self.initialPoint[1]

    def set_string(self, string):
        self.string = string

    def set_initialPoint(self, x, y):
        self.initialPoint = (x, y)

    def __evalFunction(self, xArray, yArray) -> tuple:
        try:
            # yArray = eval(self.string, {'t': xArray, 'y': yArray, 'np': np, 'math': math} ) if not(self.__isDigit) else [float(self.string)]*len(xArray)
            yArray = eval(self.string, {'t': xArray, 'y': yArray, 'np': np, 'math': math})
            return (xArray, yArray)
        except:
            print("Not valid")
            raise Exception("Not valid")

    def __plotStep(self, x, y, xi, yi):
        return([x, xi], [y, yi])
        
    def eulerMethod(self, plot_callback):
        xRange = np.arange(self.initialPoint[0], 20, self.__step)
        yi = self.initialPoint[1]
        try:
            for i in range(len(xRange)-1):
                m = self.__evalFunction(xRange[i], yi)[1]
                data = self.__plotStep(xRange[i], yi, xRange[i+1], yi+(m*self.__step))
                plot_callback(data[0], data[1], color='#FF0000')
                yi+=m*self.__step
        except:
            print("Invalid function")
            raise Exception("Not valid")
        
        xRange = np.arange(self.initialPoint[0], -20, self.__step*(-1))
        yi = self.initialPoint[1]
        try:
            for i in range(len(xRange)-1):
                m = self.__evalFunction(xRange[i], yi)[1]
                data = self.__plotStep(xRange[i], yi, xRange[i+1], yi-(m*self.__step))
                plot_callback(data[0], data[1], color='#FF0000')
                yi-=m*self.__step
        except:
            print("Invalid function")
            raise Exception("Not valid")


def createFunction(string: str) ->Function:
    return Function(string)
