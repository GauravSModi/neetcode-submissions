class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for every number, check the row, check the column, check the 3x3 grid

        # Check rows
        for i in range(9):
            rowSet = set()
            for j in range(9):
                curr = board[i][j]
                if curr != "." :
                    if curr in rowSet:
                        return False
                    else:
                        rowSet.add(curr)

        # Check columns
        for i in range(9):
            columnSet = set()
            for j in range(9):
                curr = board[j][i]
                if curr != ".":
                    if curr in columnSet:
                        return False
                    else:
                        columnSet.add(curr)

        # Check squares
        for i in range(9):
            squareSet = set()
            for j in range(3):
                for k in range(3):
                    row = ((i // 3) * 3) + j
                    col = ((i % 3) * 3) + k
                    curr = board[row][col]
                    if curr != ".":
                        if curr in squareSet:
                            return False
                        else:
                            squareSet.add(curr)

        return True