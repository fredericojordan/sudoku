'''
Created on 27 de abr de 2016

@author: fvj
'''
import copy
import random
import math

class SudokuBoard(list):
    EMPTY_POS = ' '
    SYMBOLS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
#     SYMBOLS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    def __init__(self):
        self.setup_initial_board()
            
    def setup_initial_board(self):
#         self.setup_sample_board_01()
#         self.setup_sample_board_02()
#         self.setup_sample_board_03()
        self.setup_empty_board()

    def setup_empty_board(self):
        del self[:]
        for _ in range(len(SudokuBoard.SYMBOLS)):
            self.append([SudokuBoard.EMPTY_POS for _ in range(len(SudokuBoard.SYMBOLS))])
        
    def setup_sample_board_01(self):
        del self[:]
        self.append([' ', ' ', ' ', '6', ' ', '5', ' ', ' ', ' ', ' ', '4', ' ', '1', ' ', ' ', ' '])
        self.append([' ', ' ', ' ', '5', '4', ' ', 'C', ' ', ' ', '1', ' ', 'F', '2', ' ', ' ', ' '])
        self.append([' ', ' ', ' ', '1', '7', '2', '3', ' ', ' ', '6', '8', 'A', 'E', ' ', ' ', ' '])
        self.append([' ', '2', '4', ' ', 'E', ' ', 'D', '6', '3', 'B', ' ', '7', ' ', '5', 'A', ' '])
        self.append(['9', ' ', 'B', ' ', ' ', '3', ' ', ' ', ' ', ' ', '7', ' ', ' ', '8', 'C', '0'])
        self.append(['5', ' ', '1', ' ', '0', ' ', '9', '8', '2', '4', ' ', 'D', ' ', ' ', ' ', '7'])
        self.append(['3', ' ', '7', ' ', 'F', 'D', ' ', ' ', ' ', ' ', '1', ' ', '4', '2', ' ', 'E'])
        self.append([' ', ' ', ' ', ' ', '2', ' ', '6', ' ', ' ', '0', 'F', 'C', ' ', '3', ' ', ' '])
        self.append([' ', ' ', ' ', ' ', 'D', ' ', '2', ' ', ' ', '7', ' ', '9', ' ', 'B', ' ', ' '])
        self.append(['2', ' ', '5', 'C', ' ', '8', ' ', ' ', ' ', ' ', '6', ' ', 'F', '1', ' ', '4'])
        self.append(['E', ' ', '0', ' ', '6', ' ', '5', '3', '4', 'F', ' ', '1', ' ', ' ', ' ', 'A'])
        self.append(['6', ' ', 'F', ' ', ' ', 'C', '1', ' ', ' ', '5', 'B', ' ', ' ', 'D', 'E', '2'])
        self.append([' ', '0', '6', ' ', '3', ' ', ' ', 'B', '8', 'D', 'A', '2', ' ', 'F', '5', ' '])
        self.append([' ', ' ', ' ', 'A', '5', ' ', '8', '2', '7', ' ', ' ', 'B', 'C', ' ', ' ', ' '])
        self.append([' ', ' ', ' ', '7', ' ', '9', ' ', ' ', ' ', ' ', 'E', ' ', 'B', ' ', ' ', ' '])
        self.append([' ', ' ', ' ', '8', 'C', ' ', ' ', ' ', ' ', ' ', ' ', '4', 'A', ' ', ' ', '3'])
        
    def setup_sample_board_02(self):
        del self[:]
        self.append(['5', 'C', 'B', 'F',  ' ', ' ', '9', ' ',  ' ', '0', ' ', ' ',  '7', ' ', ' ', 'D'])
        self.append(['E', '4', '1', '7',  'B', ' ', ' ', 'F',  ' ', ' ', ' ', '3',  ' ', ' ', '2', '0'])
        self.append(['8', '2', '3', 'D',  'C', ' ', 'E', '0',  '4', 'A', 'B', '5',  '6', ' ', '9', 'F'])
        self.append(['0', 'A', '6', '9',  '8', '1', '2', ' ',  'F', 'C', '7', ' ',  '5', 'B', '4', '3'])

        self.append(['A', '6', '9', '0',  '7', '2', '5', '4',  'B', 'F', '3', 'D',  '8', 'C', '1', 'E'])
        self.append(['4', 'F', '5', '3',  ' ', 'C', 'D', 'B',  'E', '1', '0', '8',  '9', '2', ' ', '7'])
        self.append(['C', 'D', '7', 'B',  ' ', ' ', '0', ' ',  ' ', ' ', ' ', ' ',  'F', ' ', ' ', '5'])
        self.append(['1', 'E', '2', '8',  '6', '9', ' ', ' ',  '5', '4', 'C', ' ',  ' ', 'D', ' ', 'B'])
        
        self.append(['F', ' ', '0', ' ',  ' ', 'D', ' ', ' ',  '8', ' ', '2', 'C',  '3', 'E', 'B', '6'])
        self.append(['2', ' ', ' ', '1',  ' ', ' ', ' ', 'C',  ' ', ' ', '6', 'F',  'A', '7', 'D', '4'])
        self.append([' ', ' ', '4', '5',  '2', 'F', '8', 'E',  'A', ' ', ' ', 'B',  '1', '9', '0', 'C'])
        self.append([' ', 'B', 'C', ' ',  '3', 'A', '6', ' ',  '0', '9', ' ', ' ',  '2', 'F', '5', '8'])
        
        self.append(['9', '1', 'D', '4',  'E', '6', 'C', '5',  '7', '2', 'F', ' ',  'B', '3', '8', 'A'])
        self.append(['7', ' ', 'E', 'C',  '0', 'B', '3', '2',  '1', ' ', '4', ' ',  'D', '6', 'F', '9'])
        self.append(['B', ' ', 'F', ' ',  ' ', ' ', ' ', ' ',  'C', ' ', 'E', ' ',  '4', '5', '7', '2'])
        self.append([' ', ' ', ' ', '2',  'F', ' ', '7', '9',  ' ', ' ', ' ', ' ',  'E', '0', 'C', '1'])
        
    def setup_sample_board_03(self):
        del self[:]
        self.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
        self.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '2', ' ', '8', '3'])
        self.append([' ', ' ', ' ', ' ', '7', ' ', ' ', ' ', ' ', ' ', ' ', '0', 'B', ' ', ' ', 'F'])
        self.append([' ', ' ', ' ', ' ', ' ', 'B', '9', ' ', ' ', '1', ' ', ' ', '6', 'A', ' ', 'D'])
        self.append([' ', ' ', ' ', ' ', ' ', ' ', '4', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' '])
        self.append([' ', ' ', ' ', '7', ' ', ' ', ' ', 'D', ' ', ' ', '2', ' ', 'A', '3', ' ', ' '])
        self.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', '5', '3', ' ', ' ', ' ', '1', 'B', 'D', '8'])
        self.append([' ', ' ', ' ', 'F', '8', ' ', ' ', ' ', '1', 'A', 'D', '6', ' ', '9', '2', '0'])
        self.append([' ', ' ', 'D', '3', ' ', ' ', 'A', ' ', ' ', ' ', ' ', 'B', ' ', ' ', ' ', ' '])
        self.append([' ', ' ', '0', ' ', ' ', ' ', '1', ' ', ' ', ' ', ' ', 'C', ' ', '4', ' ', ' '])
        self.append([' ', ' ', 'A', '1', ' ', 'C', ' ', ' ', '0', 'E', ' ', 'D', '5', '6', ' ', '9'])
        self.append([' ', ' ', '8', '6', '4', ' ', 'E', ' ', ' ', 'F', ' ', '2', ' ', '0', 'C', 'A'])
        self.append([' ', '7', ' ', ' ', ' ', ' ', 'D', '1', ' ', '2', ' ', 'E', ' ', ' ', '4', ' '])
        self.append([' ', '8', 'E', '0', ' ', '9', ' ', ' ', 'B', ' ', '6', ' ', ' ', ' ', 'F', ' '])
        self.append([' ', '1', '5', 'D', 'F', ' ', 'C', '6', ' ', ' ', '3', '4', ' ', '8', ' ', 'E'])
        self.append([' ', '4', '6', ' ', ' ', '5', ' ', ' ', 'F', ' ', 'A', '7', '9', 'C', ' ', '1'])
        
    
    def _print(self):
        for i in range(len(SudokuBoard.SYMBOLS)):
            print( str(self[i]) )
        print()
    
    def get_symbol(self, pos):
        return self[pos[0]][pos[1]]
    
    def is_pos_empty(self, pos):
        return self.get_symbol(pos) == SudokuBoard.EMPTY_POS
    
    def is_board_full(self):
        for pos in self.get_all_positions():
            if self.is_pos_empty(pos):
                return False
        return True
            
    def solve(self):
#         return self.populate_boxes()
        return self.populate_via_global_min()
    
    def populate_via_global_min(self):
        while not self.is_board_full():
            min_pos = self.get_global_min()
            if self.fill_pos(min_pos) == False:
                return False
        return True
    
    def populate_boxes(self):
        for i in range(len(SudokuBoard.SYMBOLS)):
#             if self.populate_box_sequencial(i) == False:
            if self.populate_box_from_min(i) == False:
                return False
        return True
            
    def get_box_size(self):
        return int(math.sqrt(len(SudokuBoard.SYMBOLS)))
    
    def populate_box_sequencial(self, box_num):
        for position in self.get_positions_from_box(box_num):
            if self.fill_pos(position) == False:
                return False
        return True
            
    def populate_box_from_min(self, box_num):
        while not self.is_box_full(box_num):
            min_pos = self.get_min_from_box(box_num)
            if self.fill_pos(min_pos) == False:
                return False
        return True
    
    def is_box_empty(self, bom_num):
        for pos in self.get_positions_from_box(bom_num):
            if not self.is_pos_empty(pos):
                return False
        return True
    
    def is_box_full(self, box_num):
        for pos in self.get_positions_from_box(box_num):
            if self.is_pos_empty(pos):
                return False
        return True
    
    def get_min_from_box(self, box_num):
        return self.get_min(self.get_positions_from_box(box_num))
    
    def get_global_min(self):
        return self.get_min(self.get_all_positions())
    
    def get_min(self, position_list):
        min_c = len(SudokuBoard.SYMBOLS)
        for pos in position_list:
            if not self.is_pos_empty(pos):
                continue
            count = self.count_candidates(pos)
            if count <= min_c:
                min_c = count
                min_pos = pos
        return min_pos
        
    
    def get_all_positions(self):
        return [ (i,j) for i in range(len(SudokuBoard.SYMBOLS)) for j in range(len(SudokuBoard.SYMBOLS)) ]
    
    def get_all_positions_random(self):
        pos_list = self.get_all_positions()
        random.shuffle(pos_list)
        return pos_list
    
    def fill_pos(self, position):
        if not self.is_pos_empty(position):
            return True
        else:
#             return self.fill_in_certain(position)
            return self.fill_in_random(position)
    
    def fill_in_certain(self, position):
        candidates = self.get_candidates(position)

        if len(candidates) == 1:
            self[position[0]][position[1]] = candidates[0]
            return True
        else:
#             print(position) #debug
            return False
    
    def fill_in_random(self, position):
        candidates = self.get_candidates(position)
        
        if len(candidates) < 1:
#             print(position) #debug
            return False
        else:
            i = random.randint(0,len(candidates)-1)
            self[position[0]][position[1]] = candidates[i]
            return True
    
    
    def get_candidates(self, position):
        candidates = copy.deepcopy(SudokuBoard.SYMBOLS)
        
        self.remove_same_row(candidates, position)
        self.remove_same_col(candidates, position)
        self.remove_same_box(candidates, position)
        
        return candidates
    
    def count_candidates(self, position):
        return len(self.get_candidates(position))
            
    def remove_same_row(self, candidates, position):
        for row_pos in self.get_same_row(position):
            s = self.get_symbol(row_pos)
            if s in candidates:
                candidates.remove(s)
    
    def remove_same_col(self, candidates, position):           
        for col_pos in self.get_same_col(position):
            s = self.get_symbol(col_pos)
            if s in candidates:
                candidates.remove(s)
    
    def remove_same_box(self, candidates, position):
        for box_pos in self.get_same_box(position):
            s = self.get_symbol(box_pos)
            if s in candidates:
                candidates.remove(s)
                
    def get_positions_from_box(self, box_num):
        box_size = self.get_box_size()
        a = int(box_num/box_size)
        b = box_num%box_size
        return [ (box_num+box_size*a, j+box_size*b) for box_num in range(box_size) for j in range(box_size) ]
        
    def get_box_from_position(self, pos):
        box_size = self.get_box_size()
        a = int(pos[0]/box_size)
        b = int(pos[1]/box_size)
        return b+a*box_size
    
    def get_same_box(self, pos):
        return self.get_positions_from_box(self.get_box_from_position(pos))
    
    def get_same_col(self, pos):
        return [ (i, pos[1]) for i in range(len(SudokuBoard.SYMBOLS)) ]
        
    def get_same_row(self, pos):
        return [ (pos[0], i) for i in range(len(SudokuBoard.SYMBOLS)) ]
    
    def clear_symbol(self, pos):
        self[pos[0]][pos[1]] = SudokuBoard.EMPTY_POS
        
    def set_symbol(self, pos, symbol):
        self[pos[0]][pos[1]] = symbol
    
    def minimize(self):
#         self.minimize_sequential()
        self.minimize_random()
        
    def minimize_sequential(self):
        for pos in self.get_all_positions():
            if self.is_pos_empty(pos):
                continue
            test_board = copy.deepcopy(self)
            test_board.clear_symbol(pos)
            if test_board.solve():
                self.clear_symbol(pos)
    
    def minimize_random(self):
        for pos in self.get_all_positions_random():
            if self.is_pos_empty(pos):
                continue
            test_board = copy.deepcopy(self)
            test_board.clear_symbol(pos)
            if test_board.solve():
                self.clear_symbol(pos)
#                 self._print() # debug
    
    def empty_count(self):
        count = 0
        for pos in self.get_all_positions():
            if self.is_pos_empty(pos):
                count += 1
        return count
    
    def filled_count(self):
        count = 0
        for pos in self.get_all_positions():
            if not self.is_pos_empty(pos):
                count += 1
        return count
    
    def generate_random_puzzle(self):
        b.setup_empty_board()
        while not b.solve():
            b.setup_empty_board()
        print("Solution:")
        self._print()
        self.minimize()

b = SudokuBoard()
b._print()
b.generate_random_puzzle()
b._print()
