'''
Created on 27 de abr de 2016

@author: fvj
'''
import copy
import random
import math

class SudokuBoard(list):
    random = False
    EMPTY_POS = ' '
    SYMBOLS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
#     SYMBOLS = ['F', '7', 'E', 'D', '8', 'B', '1', 'C', '4', '2', 'A', '9', '6', '0', '5', '3']
#     SYMBOLS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    def __init__(self):
        self.create_empty_positions()
        
    def create_empty_positions(self):
        del self[:]
        for _ in range(len(SudokuBoard.SYMBOLS)):
            self.append([SudokuBoard.EMPTY_POS for _ in range(len(SudokuBoard.SYMBOLS))])
    
    def _print(self):
        for i in range(len(SudokuBoard.SYMBOLS)):
            print( str(self[i]) )
    
    def get_pos(self, pos):
        return self[pos[0]][pos[1]]
            
    def populate(self):
        for i in range(len(SudokuBoard.SYMBOLS)):
            self.populate_box(i)
            
    def get_box_size(self):
        return int(math.sqrt(len(SudokuBoard.SYMBOLS)))
    
    def populate_box(self, i):
        for position in self.get_positions_from_box(i):
            self.fill_in_position(position)
            
    def fill_in_position(self, position):
        if not self.get_pos(position) == SudokuBoard.EMPTY_POS:
            return
        
        candidates = self.get_candidates(position)
        
        if len(candidates) < 1:
            self._print()
            raise Exception('No valid symbol for position ' + str(position))
        else:
            if SudokuBoard.random == True:
                i = random.randint(0,len(candidates)-1)
            else:
                i = 0
            self[position[0]][position[1]] = candidates[i]
    
    def get_candidates(self, position):
        candidates = copy.deepcopy(SudokuBoard.SYMBOLS)
        
        self.remove_same_row(candidates, position)
        self.remove_same_col(candidates, position)
        self.remove_same_box(candidates, position)
        
        return candidates
            
    def remove_same_row(self, candidates, position):
        for row_pos in self.get_same_row(position):
            s = self.get_pos(row_pos)
            if s in candidates:
                candidates.remove(s)
    
    def remove_same_col(self, candidates, position):           
        for col_pos in self.get_same_col(position):
            s = self.get_pos(col_pos)
            if s in candidates:
                candidates.remove(s)
    
    def remove_same_box(self, candidates, position):
        for box_pos in self.get_same_box(position):
            s = self.get_pos(box_pos)
            if s in candidates:
                candidates.remove(s)
                
    def get_positions_from_box(self, i):
        bs = self.get_box_size()
        a = int(i/bs)
        b = i%bs
        return [ (i+bs*a, j+bs*b) for i in range(bs) for j in range(bs) ]
        
    def get_box_from_position(self, pos):
        bs = self.get_box_size()
        a = int(pos[0]/bs)
        b = int(pos[1]/bs)
        return b+bs*a
    
    def get_same_box(self, pos):
        return self.get_positions_from_box(self.get_box_from_position(pos))
    
    def get_same_col(self, pos):
        return [ (i, pos[1]) for i in range(len(SudokuBoard.SYMBOLS)) ]
        
    def get_same_row(self, pos):
        return [ (pos[0], i) for i in range(len(SudokuBoard.SYMBOLS)) ]

b = SudokuBoard()
b.populate()
b._print()