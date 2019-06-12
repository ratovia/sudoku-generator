import numpy as np
from sudoku import Sudoku as Sudoku

"""
 
             _                  _               
            | |                | |              
   ___  ___ | |_   _____    ___| | __ _ ___ ___ 
  / __|/ _ \| \ \ / / _ \  / __| |/ _` / __/ __|
  \__ \ (_) | |\ V /  __/ | (__| | (_| \__ \__ \
  |___/\___/|_| \_/ \___|  \___|_|\__,_|___/___/
                                                
                                                
 
"""
class Solve(Sudoku):
    def __init__(self,_table):
        self.question = np.array(_table)
        self.answer = np.copy(self.question)
        self.result = False
        self.solve(self.question)
        
    def solve(self,_table):
        table = np.copy(_table)
        zero_position = self.get_zero_position(_table)
        print(zero_position)
        loop_count = 0
        while len(zero_position) > 0 and len(zero_position) >= loop_count - 5:
            target_position = zero_position.pop(0)
            uninsertable = np.concatenate(
                                            (
                                                self.get_uninsertable_by_row(table,target_position),
                                                self.get_uninsertable_by_column(table,target_position),
                                                self.get_uninsertable_by_block(table,target_position),
                                            ),
                                            axis=None
                                        )
            uninsertable = np.unique(uninsertable)
            insertable = []
            for i in range(1,10,1):
                if not i in uninsertable:
                    insertable.append(i)
            if len(insertable) == 1:
                table[target_position[0]][target_position[1]] = insertable[0]
                loop_count = 0
            else:
                zero_position.append(target_position)
                loop_count += 1
        print(self.get_zero_position(table))
        if not self.get_zero_position(table):
            self.result = True
        else:
            self.result = False    
        self.answer = np.copy(table)
    
    def get_zero_position(self,_table):
        result = []
        for i in range(9):
            for j in range(9):
                if not _table[i][j]:
                    result.append([i,j])
        return result
    
    def get_uninsertable_by_row(self,_table,pos):
        result = []
        for i in range(1,10):
            if i in _table[pos[0]]:
                result.append(i)
        return result

    def get_uninsertable_by_column(self,_table,pos):
        _table = _table.T
        result = []
        for i in range(1,10):
            if i in _table[pos[1]]:
                result.append(i)
        return result

    def get_uninsertable_by_block(self,_table,pos):
        _table = _table[(3*(pos[0]//3)):(3*(pos[0]//3)+3) , (3*(pos[1]//3)):(3+3*(pos[1]//3))]
        _table = np.reshape(_table,9)
        result = []
        for i in range(1,10):
            if i in _table:
                result.append(i)
        return result

    def display_result(self,_table):
        if self.result and self.test_format(_table):
            print("### solve ###")
        else:
            print("xxx not solve xxx")
