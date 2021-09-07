# https://leetcode.com/problems/maximal-square/
class Solution(object):
    def maximalSquare(self, matrix):
        maxSq = 0
        
        # Having to cast to zero slows it down
        # can avoid casting, but have to write to a new space which increases space complexity to O(m*n) instead of O(1)
        # run complexity: O(m*n)
        for y in range( len(matrix) ):
            for x in range( len(matrix[0]) ):
                if x > 0 and y > 0 and matrix[y][x] == "1":
                    matrix[y][x] = min(int(matrix[y-1][x-1]), int(matrix[y-1][x]), int(matrix[y][x-1])) + 1
                maxSq = max(maxSq, int(matrix[y][x]))
                    
        return maxSq ** 2
                    
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        