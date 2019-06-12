from sudoku import Sudoku as Sudoku
from solve import Solve as Solve
"""
 
                   _                        _   _               _ 
                  (_)                      | | | |             | |
   _ __ ___   __ _ _ _ __    _ __ ___   ___| |_| |__   ___   __| |
  | '_ ` _ \ / _` | | '_ \  | '_ ` _ \ / _ \ __| '_ \ / _ \ / _` |
  | | | | | | (_| | | | | | | | | | | |  __/ |_| | | | (_) | (_| |
  |_| |_| |_|\__,_|_|_| |_| |_| |_| |_|\___|\__|_| |_|\___/ \__,_|
                                                                  
                                                                  
 
"""
# 問題生成
sudoku = Sudoku()
# 問題を解く/解くことができるか確認する
solve = Solve(sudoku.get_question())
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
solve.display(solve.get_question())

# solve結果
print("answer")
ans = solve.get_answer()
solve.display(ans)
solve.display_result(ans)