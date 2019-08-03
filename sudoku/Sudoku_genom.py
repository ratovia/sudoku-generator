from sudoku import Sudoku
from decimal import Decimal
import numpy as np

class Sudoku_genom(Sudoku.Sudoku):
    def __init__(self,_table,evaluation):
        self.genom = _table
        self.evaluation = evaluation

    def getGenom(self):
        return self.genom

    def getEvaluation(self):
        return self.evaluation

    def setGenom(self, genom):
        self.genom = genom

    def setEvaluation(self, evaluation):
        self.evaluation = evaluation
    
    def EvaluationRow(self):
        result = []
        for i in range(0,9):
            result.append(1 - (9 - Decimal(len(np.unique(self.genom[i])))) / Decimal(9.0))
        return result
    def EvaluationColumn(self):
        table = self.genom.T
        result = []
        for i in range(0,9):
            result.append(1 - (9 - Decimal(len(np.unique(table[i])))) / Decimal(9.0))
        return result
    def EvaluationBlock(self):
        result = []
        array = []
        for i in range(0,3):
          for j in range(0,3):
            for _i in range(0,3):
              for _j in range(0,3):
                array.append(self.genom[i*3 + _i][j*3 + _j])
            result.append(1 - (9 - Decimal(len(array))) / Decimal(9.0))
            array = []
        return result
    def createEvaluationList(self,_table):
        result = self.EvaluationRow() + self.EvaluationColumn()
        return result