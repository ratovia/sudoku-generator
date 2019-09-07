# -*- coding: utf-8 -*-
import unittest
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(".")))
from sudoku import *
import numpy as np

class TestSudoku(unittest.TestCase):
    def setUp(self):
        self.sudoku = Sudoku.Sudoku()
    def test_question(self):
        print('question is sudoku format?')
        message = self.sudoku.test_format(self.sudoku.get_question())
        self.assertTrue(message)
    def test_answer(self):
        print('answer is sudoku format?')
        message = self.sudoku.test_format(self.sudoku.get_answer())
        self.assertTrue(message)
    def test_zero_position(self):
        print('zero position is correct?')
        self.sudoku = np.array([ 
                        [1,5,2,7,6,4,8,3,9],
                        [7,4,6,3,9,8,1,2,5],
                        [8,9,3,1,2,5,4,7,6],
                        [6,7,4,9,0,3,2,5,1],
                        [3,8,9,2,5,1,7,6,4],
                        [2,1,5,6,4,7,3,9,8],
                        [4,6,7,8,3,9,5,1,2],
                        [5,2,1,4,7,6,9,8,3],
                        [9,3,8,5,1,2,6,4,0] 
                    ])
        
        solve = Solve.Solve(self.sudoku)
        message = str(solve.get_zero_position(self.sudoku))
        self.assertEqual(message, "[[3, 4], [8, 8]]")
    def test_set_random(self):
        print('set random is success?')
        self.sudoku = np.array([ 
                        [1,5,2,7,6,4,8,3,9],
                        [7,4,6,3,9,8,1,2,5],
                        [8,9,3,1,2,5,4,7,6],
                        [6,7,4,9,0,3,2,5,1],
                        [3,8,9,2,5,1,7,6,4],
                        [2,1,5,6,4,7,3,9,8],
                        [4,6,7,8,3,9,5,1,2],
                        [5,2,1,4,7,6,9,8,3],
                        [9,3,8,5,1,2,6,4,0] 
                    ])
        solve = Solve.Solve(self.sudoku)
        table = solve.set_random(self.sudoku)
        self.assertNotEqual(table[3][4], 0)
        self.assertNotEqual(table[8][8], 0)

    def test_evaluation(self):
        print('evaluation is precision?')
        # self.sudoku = np.array([ 
        #                 [1,5,2,7,6,4,8,3,9],
        #                 [7,4,6,3,9,8,1,2,5],
        #                 [8,9,3,1,2,5,4,7,6],
        #                 [6,7,4,9,8,3,2,5,1],
        #                 [3,8,9,2,5,1,7,6,4],
        #                 [2,1,5,6,4,7,3,9,8],
        #                 [4,6,7,8,3,9,5,1,2],
        #                 [5,2,1,4,7,6,9,8,3],
        #                 [9,3,8,5,1,2,6,4,7] 
        #             ])
        self.sudoku = np.array([
                        [3, 8, 6, 4, 5, 9, 7, 1, 2],
                        [5, 4, 9, 7, 1, 2, 6, 3, 8],
                        [2, 7, 1, 3, 8, 6, 9, 5, 4],
                        [9, 5, 4, 2, 1, 7, 8, 6, 3],
                        [1, 2, 7, 8, 3, 6, 4, 9, 5],
                        [6, 3, 8, 9, 4, 5, 2, 7, 1],
                        [4, 9, 5, 1, 7, 2, 3, 8, 6],
                        [7, 1, 2, 3, 6, 8, 5, 4, 9],
                        [8, 6, 3, 5, 9, 4, 1, 2, 7]
                    ])
        genom = Sudoku_genom.Sudoku_genom(self.sudoku,0)
        solve = Genetic_solve.Genetic_solve(genom.getGenom())
        eva = solve.evaluation(genom)
        print(genom.EvaluationRow())
        print(genom.EvaluationColumn())
        print(genom.EvaluationBlock())
        self.assertEqual(eva, 1.0)
if __name__ == '__main__':
    unittest.main()