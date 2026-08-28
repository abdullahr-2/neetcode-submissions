class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.valid = True
        for i in range(len(board)):
            for j in range(len(board)):
                if i % 3 == 0 and j % 3 == 0:
                    self.check_box(board, i, j)
                self.check_row(board, i)
                self.check_col(board, j)
                if self.valid == False:
                    return False
        return True

    def check_box(self, board: List[List[str]], i: int, j: int):
        nums = []
        for k in range(i, i+3):
            for l in range(j, j+3):
                n = board[k][l] 
                if n != '.':
                    if n in nums:
                        self.valid = False
                        return
                    else:
                        nums.append(n)
        

    def check_row(self, board: List[List[str]], row: int):
        nums = []
        for i in range(len(board)):
            n = board[row][i]
            if n != '.':
                if n in nums:
                    self.valid = False
                    return
                else:
                    nums.append(n)

    def check_col(self, board: List[List[str]], col: int):
        nums = []
        for i in range(len(board)):
            n = board[i][col]
            if n != '.':
                if n in nums:
                    self.valid = False
                    return
                else:
                    nums.append(n)