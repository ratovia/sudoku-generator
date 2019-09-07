# -*- coding: utf-8 -*-
import random
from decimal import Decimal
from sudoku import Solve
from sudoku import Sudoku_genom
import numpy as np

MAX_GENOM_LIST = 100
SELECT_GENOM = 20
INDIVIDUAL_MUTATION = 0.05
GENOM_MUTATION = 0.08
MAX_GENERATION = 1000

class Genetic_solve(Solve.Solve):
    def __init__(self,_table):
        self.question = np.array(_table)
        self.answer = np.copy(self.question)
        self.result = False
        self.solve(np.copy( self.question))

    def create_genom(self,_table):
        return Sudoku_genom.Sudoku_genom(_table,0)


    def evaluation(self,genom):
        """
        評価関数
        """
        evaluation_list = genom.createEvaluationList(genom.getGenom())
        genom_total = sum(evaluation_list)
        return Decimal(genom_total) / Decimal(len(evaluation_list))


    def select(self,genoms, elite):
        """
        選択関数
        """
        sort_result = sorted(genoms, reverse=True, key=lambda u: u.evaluation)
        result = [sort_result.pop(0) for i in range(elite)]
        return result


    def crossover(self,_table,genom_A, genom_B):
        """
        交叉関数
        2つのSudoku_genom子孫を作成し、リスト返す
        オリジナルの空きマスには
        ・エリートA
        ・エリートB
        のいずれかが継承して入る
        """
        zero_position = self.get_zero_position(_table)
        genom_list = []
        progeny_one = np.copy(_table)
        progeny_second = np.copy(_table)
        while len(zero_position) > 0:
            target_position = zero_position.pop(0)
            if random.randint(0,1):
                progeny_one[target_position[0]][target_position[1]] = genom_A.genom[target_position[0]][target_position[1]]
                progeny_second[target_position[0]][target_position[1]] = genom_B.genom[target_position[0]][target_position[1]]
            else:
                progeny_one[target_position[0]][target_position[1]] = genom_B.genom[target_position[0]][target_position[1]]
                progeny_second[target_position[0]][target_position[1]] = genom_A.genom[target_position[0]][target_position[1]]
        genom_list.append(Sudoku_genom.Sudoku_genom(progeny_one, 0))
        genom_list.append(Sudoku_genom.Sudoku_genom(progeny_second, 0))
        return genom_list

    def crossover2(self,_table,genom_A, genom_B):
        """
        交叉関数です。
        3つのSudoku_genom子孫を作成し、リスト返す
        オリジナルの空きマスには
        ・エリートA
        ・エリートB
        のいずれかを列ごと、行ごと、ブロックごとに継承して入る
        """
        genom_list = []
        progeny_one = np.copy(_table)
        progeny_second = np.copy(_table)
        progeny_three = np.copy(_table)
        for i in range(0,9):
            if genom_A.EvaluationRow()[i] > genom_B.EvaluationRow()[i]:
                progeny_one[i] = genom_A.getGenom()[i]
            else:
                progeny_one[i] = genom_B.getGenom()[i]

            if genom_A.EvaluationColumn()[i] > genom_B.EvaluationColumn()[i]:
                progeny_second = progeny_second.T
                table = genom_A.getGenom().T
                progeny_second[i] = table[i]
                progeny_second = progeny_second.T
            else:
                progeny_second = progeny_second.T
                table = genom_B.getGenom().T
                progeny_second[i] = table[i]
                progeny_second = progeny_second.T
        for i in range(0,3):
            for j in range(0,3):
                if genom_A.EvaluationBlock()[i*3 + j] > genom_B.EvaluationBlock()[i*3 + j]:
                    for _i in range(0,3):
                        for _j in range(0,3):
                            progeny_three[i*3 + _i][j*3 + _j] = genom_A.getGenom()[i*3 + _i][j*3 + _j]
                else:
                    for _i in range(0,3):
                        for _j in range(0,3):
                            progeny_three[i*3 + _i][j*3 + _j] = genom_B.getGenom()[i*3 + _i][j*3 + _j]
            
        genom_list.append(Sudoku_genom.Sudoku_genom(progeny_one, 0))
        genom_list.append(Sudoku_genom.Sudoku_genom(progeny_second, 0))
        genom_list.append(Sudoku_genom.Sudoku_genom(progeny_three, 0))
        return genom_list

    def next_generation_gene_create(self,ga, ga_elite, ga_progeny):
        """
        世代交代
        """
        next_genoms = sorted(ga, reverse=False, key=lambda u: u.evaluation)
        for i in range(0, len(ga_elite) + len(ga_progeny)):
            next_genoms.pop(0)
        next_genoms.extend(ga_elite)
        next_genoms.extend(ga_progeny)
        return next_genoms


    def mutation(self,_table,genoms, induvidual_mutation, genom_mutation):
        """
        突然変異
        数独のランダムの場所が突然変異する。
        """
        genom_list = []
        for genom in genoms:
            if induvidual_mutation > (random.randint(0, 100) / Decimal(100)):
                genom.setGenom(self.set_random(_table))

            zero_position = self.get_zero_position(_table)
            while len(zero_position) > 0:
                target_position = zero_position.pop(0)
                if genom_mutation > (random.randint(0, 100) / Decimal(100)):
                    table = genom.getGenom()
                    table[target_position[0]][target_position[1]] = random.randint(1, 9)
                    genom.setGenom(table)
            genom_list.append(genom)
        return genom_list

    def mutation2(self,_table,genoms, induvidual_mutation, genom_mutation):
        """
        突然変異
        get_zero_position(_table)
        によって入ることができる値の範囲で突然変異する。
        """
        genom_list = []
        for genom in genoms:
            if induvidual_mutation > (random.randint(0, 100) / Decimal(100)):
                genom.setGenom(self.set_random(_table))
            if genom_mutation > (random.randint(0, 100) / Decimal(100)):
                zero_position = self.get_zero_position(_table)
                random_position = random.sample(zero_position, len(zero_position))
                while len(random_position) > 0:
                    target_position = random_position.pop(0)
                    table = genom.getGenom()
                    table[target_position[0]][target_position[1]] = 0
                    genom.setGenom(table)
                genom.setGenom(self.set_random(genom.getGenom()))
            genom_list.append(genom)
        return genom_list

    def solve(self,_table):
        table = np.copy(_table)
        current_genoms = []
        for i in range(MAX_GENOM_LIST):
            current_genoms.append(self.create_genom(self.set_random(table)))
        for count_ in range(0, MAX_GENERATION):
            for i in range(MAX_GENOM_LIST):
                evaluation_result = self.evaluation(current_genoms[i])
                current_genoms[i].setEvaluation(evaluation_result)
            elite_genes = self.select(current_genoms,SELECT_GENOM)
            progeny_gene = []
            for i in range(0, SELECT_GENOM):
                progeny_gene.extend(self.crossover2(table, elite_genes[i - 1], elite_genes[i]))
            next_genoms = self.next_generation_gene_create(current_genoms,elite_genes, progeny_gene)
            next_genoms = self.mutation2(_table,next_genoms,INDIVIDUAL_MUTATION,GENOM_MUTATION)
            fits = [j.getEvaluation() for j in current_genoms]
            min_ = min(fits)
            max_ = max(fits)
            avg_ = sum(fits) / Decimal(len(fits))
            print ("-----第{}世代の結果-----".format(count_))
            print ("  Min:{}".format(min_))
            print ("  Max:{}".format(max_))
            print ("  Avg:{}".format(avg_))
            display_genes = self.select(current_genoms,1)
            # print (display_genes[0].display(display_genes[0].getGenom()))　# debug
            if max_ == 1:
                print ("######第{}世代で学習完了しました#####".format(count_))
                elite_genes = self.select(current_genoms,1)
                # print ("最も優れた個体は") # debug
                # print (elite_genes[0].display(elite_genes[0].getGenom())) # debug
                table = np.copy(elite_genes[0].getGenom())
                self.result = True
                break
            else:
                current_genoms = next_genoms
                self.result = False    
        self.answer = np.copy(elite_genes[0].getGenom())