# https://leetcode.com/problems/rotate-image/
#
# start:            [ 1 2 3 ]
#                   [ 4 5 6 ]
#                   [ 7 8 9 ]
#
# rotated (goal):   [ 7 4 1 ]
#                   [ 8 5 2 ]
#                   [ 9 6 3 ]    
# Step 1:
# transpose:        [ 1 4 7 ]
#                   [ 2 5 8 ]
#                   [ 3 6 9 ]
# Step 2:
# reversed:         [ 7 4 1 ]
#                   [ 8 5 2 ]
#                   [ 9 6 3 ]
# Done!

class Solution:
    def rotate(self, matrix):
        self.transpose(matrix)
        self.reflect(matrix)
    
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
