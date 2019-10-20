import random
import numpy as np

class Enemy:
    def block_opponent(self, helper):
        for condition in helper.win_conditions:
            matches = []
            [matches.append(element) for element in condition if element in helper.player_positions]
            if len(matches) == 2:
                space_to_block = [x for x in condition if x not in matches]
                row = int(helper.convert_integer_to_coordinates(int(space_to_block[0]))[:1])
                column = int(helper.convert_integer_to_coordinates(int(space_to_block[0]))[2:3])
                if helper.board[row, column] != 'O':
                    helper.board[row, column] = 'O'
                    return True
        return False
    
    def found_lethal(self, helper):
        for condition in helper.win_conditions:
            matches = []
            result = np.where(helper.board == 'O')
            helper.computer_positions = map(helper.convert_coordinates_to_integer, np.array(zip(result[0], result[1])))
            [matches.append(element) for element in condition if element in helper.computer_positions]
            if len(matches) == 2:
                space_to_select = [x for x in condition if x not in helper.player_positions and x not in helper.computer_positions]
                if len(space_to_select) > 0:
                    row = int(helper.convert_integer_to_coordinates(int(space_to_select[0]))[:1])
                    column = int(helper.convert_integer_to_coordinates(int(space_to_select[0]))[2:3])
                    helper.board[row, column] = 'O'
                    return True
        return False
        
    def ai(self, helper):
        if self.found_lethal(helper):
            return
        if self.block_opponent(helper):
            return
        if(any(elem in helper.player_positions for elem in helper.computer_selected_path)):
                helper.path_found = False
                helper.path_index = 0
        helper.win_conditions = list(helper.win_conditions)
        random.shuffle(helper.win_conditions)
        random.shuffle(helper.win_conditions)
        if not helper.path_found:
            for condition in helper.win_conditions:
                if not any(elem in helper.player_positions for elem in condition):
                    helper.path_found = True
                    helper.computer_selected_path = condition
        if helper.path_found:
            row = int(helper.convert_integer_to_coordinates(helper.computer_selected_path[helper.path_index])[:1])
            column = int(helper.convert_integer_to_coordinates(helper.computer_selected_path[helper.path_index])[2:3])
            helper.board[row, column] = 'O'
            helper.path_index += 1
        else:
            random_numbers = range(9)
            random.shuffle(random_numbers)
            for i in random_numbers:
                if i not in helper.player_positions and i not in helper.computer_positions:
                    row = int(helper.convert_integer_to_coordinates(i)[:1])
                    column = int(helper.convert_integer_to_coordinates(i)[2:3])
                    helper.board[row, column] = 'O'
                    break