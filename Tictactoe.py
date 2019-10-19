import numpy as np
from Helper import Helper
from Enemy import Enemy
import time

class TicTacToe:
   
    def print_board(self, helper):
        print '\n'.join(' '.join(str(cell) for cell in row ) for row in helper.board)
    
    def check_win_condition(self, symbol, helper):
        player_won = False
        result = np.where(helper.board == symbol)
        helper.player_positions = map(helper.convert_coordinates_to_integer, np.array(zip(result[0], result[1])))
        for condition in helper.win_conditions:
            if(all(elem in helper.player_positions for elem in condition)):
                player_won = True
        
        return player_won
        
    def main(self):
        enemy = Enemy()
        helper = Helper()
        self.print_board(helper)
        position = raw_input('Enter position (row # column #) : ')
        while position != 'q':
            position_to_move = tuple(position.replace(' ', ''))
            if helper.check_basic_validations(position_to_move):
                helper.board[int(position_to_move[0]), int(position_to_move[1])] = "X"
                self.print_board(helper)
                if self.check_win_condition('X', helper):
                    print 'You win!'
                    position = 'q'
                    break
                if len(helper.get_current_positions('X')) + len(helper.get_current_positions('O')) == 9:
                    print "It's a tie!"
                    break
                print '\n... Computer is thinking ...\n'
                time.sleep(1)
                enemy.ai(helper)
                self.print_board(helper)
                if self.check_win_condition('O', helper):
                    print 'Computer Wins!'
                    break
            position = raw_input('Enter position : ')        
        
if __name__ == "__main__":
    ticTacToe = TicTacToe()
    ticTacToe.main() 
    
    
