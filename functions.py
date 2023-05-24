import numpy as np
import math
class Function(object):
    def __init__(self, string:str) -> None:
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
            return (0, 0)
        

class differentialEquation(Function):
    def __init__(self, string: str, initialPoint: tuple) -> None:
        super().__init__(string) 
        self.initialPoint = initialPoint

    def __evalFunction(self, xArray, yArray = 0) -> tuple:
        try:
            yArray = eval(self.string, {'t': xArray, 'y': yArray, 'np': np, 'math': math} ) if not(self.__isDigit) else [float(self.string)]*len(xArray)
            return (xArray, yArray)
        except:
            return (0, 0)
        
    def eulerMethod(self) -> None:
        pass

        
mifuncion = Function("3*x-2")
print(mifuncion.evalFunction(np.arange(-10, 10, 1)))
