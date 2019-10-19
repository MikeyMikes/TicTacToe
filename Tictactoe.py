import numpy as np
from Helper import Helper
from Enemy import Enemy
import time

class TicTacToe:
   
    def printBoard(self, helper):
        print '\n'.join(' '.join(str(cell) for cell in row ) for row in helper.board)
    
    def checkWinCondition(self, symbol, helper):
        playerWon = False
        result = np.where(helper.board == symbol)
        helper.playerPositions = map(helper.convertCoordinatesToInteger, np.array(zip(result[0], result[1])))
        for condition in helper.winConditions:
            if(all(elem in helper.playerPositions for elem in condition)):
                playerWon = True
        
        return playerWon
        
    def main(self):
        enemy = Enemy()
        helper = Helper()
        self.printBoard(helper)
        position = raw_input('Enter position : ')
        while position != 'q':
            positionToMove = tuple(position)
            helper.board[int(positionToMove[0]), int(positionToMove[1])] = "X"
            self.printBoard(helper)
            if self.checkWinCondition('X', helper):
                print 'You win!'
                position = 'q'
                break
            if len(helper.getCurrentPositions('X')) + len(helper.getCurrentPositions('O')) == 9:
                print "It's a tie!"
                break
            print '\n... Computer is thinking ...\n'
            time.sleep(1)
            enemy.ai(helper)
            self.printBoard(helper)
            if self.checkWinCondition('O', helper):
                print 'Computer Wins!'
                break
            position = raw_input('Enter position : ')
             
        
if __name__ == "__main__":
    ticTacToe = TicTacToe()
    ticTacToe.main() 
    
    
