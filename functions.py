import numpy as np
class Function(object):
    def __init__(self, string:str, independent:str, dependent:str) -> None:
        self.string = string
        self.independent = independent
        self.dependent = dependent
        self.__isDigit = self.string.isdigit()

    #Getters
    def get_isDigit(self):
        return(self.__isDigit)

    def evalFunction(self, xArray):
        try:
            yArray = eval(self.string, {'x': xArray, 'np': np} ) if not(self.__isDigit) else [float(self.string)]*len(xArray)
            return (xArray, yArray)
        except:
            return 0
        

mifuncion = Function("3", "x", "y")
print(mifuncion.evalFunction(np.arange(-10, 10, 1)))
