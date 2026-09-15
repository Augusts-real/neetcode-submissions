class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        c_hash  = {}
        r_hash = {}
        squares = {}
        for htn in range(9):
            c_hash[htn] = []
            squares[htn] = []

        # board = [
        # [".",".","4",".",".",".","6","3","."],
        # [".",".",".",".",".",".",".",".","."],
        # ["5",".",".",".",".",".",".","9","."],
        # [".",".",".","5","6",".",".",".","."],
        # ["4",".","3",".",".",".",".",".","1"],
        # [".",".",".","7",".",".",".",".","."],
        # [".",".",".","5",".",".",".",".","."],
        # [".",".",".",".",".",".",".",".","."],
        # [".",".",".",".",".",".",".",".","."]]           # htn, i, b, r, c

        for i in range(9):
            for b in board:
                c_hash[i].append(b[i])

        for b in range(9):
            r_hash[b] = board[b]


        # counter = 0
        # addition = 0
        # for r in range(9):
        #     for c in range(9):
        #         square = (c//3) + addition
        #         # print(square)
        #         s_hash[square].append(r_hash[r][c])
        #     addition += 3
        #-------------------------
        guide = [0, 3,6]
        # counter = 0
        # for j in range(1, 10):
        #     for u in guide:
        #         squares[counter].extend(s_hash[u + counter])

            # counter += 1

        for rr_i, rr in enumerate(board):
            for cc_i, cc in enumerate(rr):
                section = cc_i//3 + ((rr_i//3)*3)
                squares[section].append(cc)


        for row_index, row in enumerate(board):
            for column_index, column in enumerate(row):
                block = column_index//3 + ((row_index//3)*3)
                if column != ".":
                    if c_hash[column_index].count(column) > 1:
                        return False # print(f"FALSE [COLUMN] because of element: {column} in column: {column_index} and row {row_index}")
                    if r_hash[row_index].count(column) > 1:
                        return False #print(f"FALSE [ROW] because of element: {column} in column: {column_index} and row {row_index}")
                    if squares[block].count(column) > 1:
                        return False #print(f"FALSE [SQUARE] because of element: {column} in column: {column_index} and row {row_index}")


        # for keys, values in squares.items():
        #     # print(f"--{keys}--")
        #     # for ff in range(0, 9, 3):
        #     #     print(values[ff:ff+3])
            #print(f"{keys} : {values}")  
        return True