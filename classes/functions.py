import numpy as np
import math

#Main structure of a function
#This functions need to have x as the independant variable
#Since the string parsing is done automatically by eval(), the input must be done in python syntax.
#I know this is a lazy solution
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
            #In case that just a number is passed as a string, the return must be treated separately to ensure that a tuple of arrays is always returned
            yArray = eval(self.string, {'x': xArray, 'np': np, 'math': math} ) if not(self.__isDigit) else [float(self.string)]*len(xArray)
            return (xArray, yArray)
        except:
            raise Exception("Not valid")
        
#Uses the euler method to "solve" a differential equation given an initial value.
#This equations only recieve y and t as variables, since they are in the form dy/dt=(...)
class differentialEquation(Function):
    def __init__(self, string: str, initialPoint: tuple) -> None:
        super().__init__(string) 
        self.initialPoint = initialPoint

        #Step for the eulers method calculations
        #The lower, the more precise. But will also take more calculations
        self.__step = 0.1 

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

    #Takes two point coordinates and returns in in a format to be plotted by matplotlib
    def __plotStep(self, x, y, xi, yi):
        return([x, xi], [y, yi])
        
    #Since the euler method needs to graph a single line per iteration, a plotting callback is needed
    def eulerMethod(self, plot_callback):
        #Starts plotting to the right of the initial point
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
        
        #Now to the left of the initial piont
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

