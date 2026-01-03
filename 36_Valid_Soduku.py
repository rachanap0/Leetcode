# You are given a 9 x 9 Sudoku board. Write a program to determine if the Sudoku is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
# The Sudoku board could be valid but is not necessarily solvable.

import collections
class Solution:
    def isValidSoduku(self, board):
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in square[(r//3, c//3)]):
                    #(r//3, c//3) to identify the 3x3 sub-boxes 
                    # eg: (0,0), (0,1), (0,2)
                    #     (1,0), (1,1), (1,2)
                    #     (2,0), (2,1), (2,2)   
                    # if any of the three conditions is true, we return false
                    return False
                

                row[r].add(board[r][c]) 
                col[c].add(board[r][c])
                square[(r//3, c//3)].add(board[r][c])
        return True
    
solution = Solution()
board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

print(solution.isValidSoduku(board))