class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        c_hash  = {}
        r_hash = {}
        squares = {}
        for htn in range(9):
            c_hash[htn] = []
            squares[htn] = []

        for i in range(9):
            for b in board:
                c_hash[i].append(b[i])

        for b in range(9):
            r_hash[b] = board[b]

        for rr_i, rr in enumerate(board):
            for cc_i, cc in enumerate(rr):
                section = cc_i//3 + ((rr_i//3)*3)
                squares[section].append(cc)

        for row_index, row in enumerate(board):
            for column_index, column in enumerate(row):
                block = column_index//3 + ((row_index//3)*3)
                if column != ".":
                    if c_hash[column_index].count(column) > 1:
                        return False 
                    if r_hash[row_index].count(column) > 1:
                        return False 
                    if squares[block].count(column) > 1:
                        return False  
        return True