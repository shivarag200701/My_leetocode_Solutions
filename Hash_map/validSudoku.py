from collections import defaultdict


class Solution(object):
    def isValidSudoku(self, board):
        row = defaultdict(list)
        column = defaultdict(list)
        square = defaultdict(list)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if (
                    (board[r][c] in row[r])
                    or (board[r][c] in column[c])
                    or (board[r][c] in square[(r // 3, c // 3)])
                ):
                    return False

                else:
                    row[r].append(board[r][c])
                    column[c].append(board[r][c])
                    square[(r // 3, c // 3)].append(board[r][c])

        return True
