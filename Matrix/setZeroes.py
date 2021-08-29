#https://leetcode.com/problems/set-matrix-zeroes/
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        height = len(matrix)
        width = len(matrix[0])
        
        for y in range(0, height):
            for x in range(0, width):
                if matrix[y][x] == 0:
                    for y2 in range(0, height):
                        if matrix[y2][x] != 0:
                            matrix[y2][x] = "z"
                    for x2 in range(0, width):
                        if matrix[y][x2] != 0:
                            matrix[y][x2] = "z"
        
        for y in range(0, height):
            for x in range(0, width):
                if matrix[y][x] == "z":
                    matrix[y][x] = 0
                    
        return None