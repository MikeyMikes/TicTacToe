import numpy as np

class Helper:
    player_positions = []
    computer_positions = []
    computer_selected_path = []
    path_index = 0
    path_found = False
    
    board = np.array([["_","_","_"],
                      ["_","_","_"],
                      ["_","_","_"]])
    
    win_conditions = np.array([[0, 3, 6],
                              [3, 4, 5],
                              [6, 7, 8],
                              [0, 1, 2],
                              [1, 4, 7],
                              [2, 5, 8],
                              [0, 4, 8],
                              [2, 4, 6]])
    
    def get_coordinate_integer_mapping(self):
        possibleCoordinates = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
        d = {}
        for i,x in enumerate(possibleCoordinates):
            d[''.join(str(x).replace('[', '').replace(']', '').replace(',', ''))] = i
            
        return d
    
    def convert_coordinates_to_integer(self, arr):
        return self.get_coordinate_integer_mapping()[''.join(str(arr).replace('[', '').replace(']', '').replace(',', ''))]
    
    def convert_integer_to_coordinates(self, num):
        for k,v in self.get_coordinate_integer_mapping().items():
            if v == num:
                return k
    
    def get_current_positions(self, symbol):
        result = np.where(self.board == symbol)
        return map(self.convert_coordinates_to_integer, np.array(zip(result[0], result[1])))


