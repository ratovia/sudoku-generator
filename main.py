# -*- coding: utf-8 -*-
from sudoku import * 
import time
from datetime import *
"""
 
                   _                        _   _               _ 
                  (_)                      | | | |             | |
   _ __ ___   __ _ _ _ __    _ __ ___   ___| |_| |__   ___   __| |
  | '_ ` _ \ / _` | | '_ \  | '_ ` _ \ / _ \ __| '_ \ / _ \ / _` |
  | | | | | | (_| | | | | | | | | | | |  __/ |_| | | | (_) | (_| |
  |_| |_| |_|\__,_|_|_| |_| |_| |_| |_|\___|\__|_| |_|\___/ \__,_|
                                                                  
                                                                  
 
"""

con = ConnectDB.ConnectDB()
timestamp = datetime.now().strftime( '%Y-%m-%d %H:%M:%S' )

for i in range(1):
# 問題生成
  puzzle = Sudoku.Sudoku()
  # 問題を解く/解くことができるか確認する
  solve = Genetic_solve.Genetic_solve(puzzle.get_question())
  # 任意の問題を使うとき
  # solve = Solve([
  #                 [0,5,0,0,9,0,0,0,0],
  #                 [4,0,0,0,0,0,1,0,0],
  #                 [1,0,0,0,0,5,0,3,0],
  #                 [0,0,7,8,0,0,0,0,9],
  #                 [5,0,0,0,0,0,0,0,7],
  #                 [9,0,0,0,4,0,3,0,0],
  #                 [0,7,0,3,0,0,0,0,6],
  #                 [0,0,6,0,0,0,0,0,4],
  #                 [0,0,0,0,2,0,0,5,0]
  #             ]
  #         )

  print("question")
  que = solve.get_question()
  solve.display(que)

  # solve結果
  print("answer")
  ans = puzzle.get_answer()
  solve.display(ans)
  solve.display_result(ans)



  if solve.get_result():
    answer = ""
    for item in ans.reshape(81).tolist():
        answer += str(item)
    question = ""
    for item in que.reshape(81).tolist():
        question += str(item)

    sql_command = 'INSERT INTO puzzles(answer,question,progress,created_at,updated_at) values ("{answer}","{question}","{progress}","{created_at}","{updated_at}")'.format(answer=answer,question=question,progress=question,created_at=timestamp,updated_at=timestamp)
    con.execute(sql_command)
    con.display()
con.close()
