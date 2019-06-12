from enum import Enum
import numpy as np
import random
"""
                 _       _          
                | |     | |         
   ___ _   _  __| | ___ | | ___   _ 
  / __| | | |/ _` |/ _ \| |/ / | | |
  \__ \ |_| | (_| | (_) |   <| |_| |
  |___/\__,_|\__,_|\___/|_|\_/\__,_|


"""     
class Sudoku():
    # 定数
    SHUFFLE_ABC   = 1
    SHUFFLE_DEF   = 2
    SHUFFLE_GHI   = 3
    SHUFFLE_123   = 4
    SHUFFLE_456   = 5
    SHUFFLE_789   = 6
    SHUFFLE_ROWS  = 7
    SHUFFLE_COLS  = 8
    SHUFFLE_NUM   = 9
    BLANK_NUM = 30

    def __init__(self):
        self.table = []
        self.answer = []
        self.question = []
        self.set_default_table()
        self.set_answer()
        self.set_question(self.answer)

    def set_default_table(self):
        self.table = np.array([
                        [1,4,7,2,5,8,3,6,9],
                        [2,5,8,3,6,9,4,7,1],
                        [3,6,9,4,7,1,5,8,2],
                        [4,7,1,5,8,2,6,9,3],
                        [5,8,2,6,9,3,7,1,4],
                        [6,9,3,7,1,4,8,2,5],
                        [7,1,4,8,2,5,9,3,6],
                        [8,2,5,9,3,6,1,4,7],
                        [9,3,6,1,4,7,2,5,8]
                    ])

    def set_answer(self):
        for i in range(1000):
            self.shuffle(random.randint(1,9),self.table)
        self.answer = self.table

    def set_blank(self,_table):
        blank_num = self.BLANK_NUM
        boolean_data = np.array([True]*81)
        boolean_data[0:blank_num] = False
        random.shuffle(boolean_data)
        filter_data = np.reshape(boolean_data,(9,9))
        for i in range(9):
            for j in range(9):
                if not filter_data[i][j]:
                    _table[i][j] = 0
        return _table

    def set_question(self,_table):
        self.table = self.set_blank(np.copy(_table))
        # TODO 解けるか確認する
        # TODO 解けるまで繰り返す
        self.question = self.table

    def get_answer(self):
        return self.answer

    def get_question(self):
        return self.question

    def display(self,_table):
        print(_table)

    def test_format(self,_table):
        column_sum = np.array([0] * 9)
        for i in range(9):
            row_sum = np.array(_table[i]).sum()
            if row_sum != 45:
                msg="This is not Sudoku format."
            column_sum += np.array(_table[i])
        if np.array([45] * 9).all() != column_sum.all():
            msg="This is not Sudoku format."
        if str(_table.shape) != "(9, 9)":
            msg="This is not Sudoku format."
        return True

    def shuffle(self,type,_table):
        def inner_shuffle_function(_table,start,end,is_transpose):
            if is_transpose:
                _table = _table.T
            transposed = _table
            partial = transposed[start:end]
            np.random.shuffle(partial)
            transposed[start:end] = partial
            if is_transpose:
                transposed = transposed.T
            _table = transposed
   
        if type == self.SHUFFLE_ABC:
            inner_shuffle_function(_table,0,3,True)
        elif type == self.SHUFFLE_DEF:
            inner_shuffle_function(_table,3,6,True)
        elif type == self.SHUFFLE_GHI:
            inner_shuffle_function(_table,6,9,True)
        elif type == self.SHUFFLE_123:
            inner_shuffle_function(_table,0,3,False)
        elif type == self.SHUFFLE_456:
            inner_shuffle_function(_table,3,6,False)
        elif type == self.SHUFFLE_789:
            inner_shuffle_function(_table,6,9,False)
        elif type == self.SHUFFLE_ROWS:
            partial = [np.copy(_table[0:3]),np.copy(_table[3:6]),np.copy(_table[6:9])]
            random.shuffle(partial)
            for i in range(3):
                _table[(0+3*i):(3+3*i)] = partial[i]
        elif type == self.SHUFFLE_COLS:
            transposed = _table.T
            partial = [np.copy(transposed[0:3]),np.copy(transposed[3:6]),np.copy(transposed[6:9])]
            random.shuffle(partial)
            for i in range(3):
                transposed[(0+3*i):(3+3*i)] = partial[i]
            _table = transposed.T
        elif type == self.SHUFFLE_NUM:
            array = [1,2,3,4,5,6,7,8,9]
            random.shuffle(array)
            for i in range(9):
                for j in range(9):
                    data = _table[i][j]
                    _table[i][j] = array[data - 1]
        else:
            print("fail")
        self.table = _table