import numpy as np

class Helper:
    playerPositions = []
    computerPositions = []
    computerSelectedPath = []
    pathIndex = 0
    pathFound = False
    
    board = np.array([["_","_","_"],
                      ["_","_","_"],
                      ["_","_","_"]])
    
    winConditions = np.array([[0, 3, 6],
                              [3, 4, 5],
                              [6, 7, 8],
                              [0, 1, 2],
                              [1, 4, 7],
                              [2, 5, 8],
                              [0, 4, 8],
                              [2, 4, 6]])
    
    def getCoordinateIntegerMapping(self):
        possibleCoordinates = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
        d = {}
        for i,x in enumerate(possibleCoordinates):
            d[''.join(str(x).replace('[', '').replace(']', '').replace(',', ''))] = i
            
        return d
    
    def convertCoordinatesToInteger(self, arr):
        return self.getCoordinateIntegerMapping()[''.join(str(arr).replace('[', '').replace(']', '').replace(',', ''))]
    
    def convertIntegerToCoordinates(self, num):
        for k,v in self.getCoordinateIntegerMapping().items():
            if v == num:
                return k
    
    def getCurrentPositions(self, symbol):
        result = np.where(self.board == symbol)
        return map(self.convertCoordinatesToInteger, np.array(zip(result[0], result[1])))


