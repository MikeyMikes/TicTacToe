import random
import numpy as np

class Enemy:
    def blockOpponent(self, helper):
        for condition in helper.winConditions:
            matches = []
            [matches.append(element) for element in condition if element in helper.playerPositions]
            if len(matches) == 2:
                spaceToBlock = [x for x in condition if x not in matches]
                row = int(helper.convertIntegerToCoordinates(int(spaceToBlock[0]))[:1])
                column = int(helper.convertIntegerToCoordinates(int(spaceToBlock[0]))[2:3])
                if helper.board[row, column] != 'O':
                    helper.board[row, column] = 'O'
                    return True
        return False
    
    def foundLethal(self, helper):
        for condition in helper.winConditions:
            matches = []
            result = np.where(helper.board == 'O')
            helper.computerPositions = map(helper.convertCoordinatesToInteger, np.array(zip(result[0], result[1])))
            [matches.append(element) for element in condition if element in helper.computerPositions]
            if len(matches) == 2:
                spaceToSelect = [x for x in condition if x not in helper.playerPositions and x not in helper.computerPositions]
                if len(spaceToSelect) > 0:
                    row = int(helper.convertIntegerToCoordinates(int(spaceToSelect[0]))[:1])
                    column = int(helper.convertIntegerToCoordinates(int(spaceToSelect[0]))[2:3])
                    helper.board[row, column] = 'O'
                    return True
        return False
        
    def ai(self, helper):
        if self.foundLethal(helper):
            return
        if self.blockOpponent(helper):
            return
        if(any(elem in helper.playerPositions for elem in helper.computerSelectedPath)):
                helper.pathFound = False
                helper.pathIndex = 0
        while not helper.pathFound:
            helper.computerSelectedPath = helper.winConditions[random.randint(0, 7)]
            if(not any(elem in helper.playerPositions for elem in helper.computerSelectedPath)):
                helper.pathFound = True  
        row = int(helper.convertIntegerToCoordinates(helper.computerSelectedPath[helper.pathIndex])[:1])
        column = int(helper.convertIntegerToCoordinates(helper.computerSelectedPath[helper.pathIndex])[2:3])
        helper.board[row, column] = 'O'
        helper.pathIndex += 1