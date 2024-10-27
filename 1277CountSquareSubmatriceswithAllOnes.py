class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        
        count = 0
        count += sum([sum(row) for row in matrix])
        
        for side in range(2, min(rows, cols) + 1):
            for i in range(side - 1, rows):
                for j in range(side - 1, cols):
                    if matrix[i][j] == 1:
                        zero = False
                        for x in range(i - side + 1, i + 1):
                            if zero:
                                break
                            for y in range(j - side + 1, j + 1):
                                if matrix[x][y] == 0:
                                    zero = True
                                    break
                        if not zero:
                            count += 1
        return count
