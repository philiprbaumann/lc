#https://leetcode.com/problems/count-square-submatrices-with-all-ones/
class Solution(object):
    def countSquares(self, matrix):
        sqCt = 0
        
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if x > 0 and y > 0 and matrix[y][x] == 1:
                    matrix[y][x] = min(matrix[y-1][x-1], matrix[y-1][x], matrix[y][x-1]) + 1
                sqCt += matrix[y][x]
                
        return sqCt
        """
        :type matrix: List[List[int]]
        :rtype: int
        """