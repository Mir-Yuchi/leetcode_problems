class Solution:
    def isValid(self, nums):
        d = {}
        for n in nums:
            if n != '.':
                if n in d:
                    return False
                d[n] = 1
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.isValid(board[i]):
                return False
        for i in range(9):
            if not self.isValid([board[j][i] for j in range(9)]):
                return False
        for i in range(3):
            for j in range(3):
                if not self.isValid([board[x][y] for x in range(3 * i, 3 * i + 3) for y in range(3 * j, 3 * j + 3)]):
                    return False
        return True
