#https://leetcode.com/problems/spiral-matrix/
class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]: 
            return []                       # Return empty if empty
        
        ans = []
        m, n = len(matrix), len(matrix[0])
        u, d, l, r = 0, m - 1, 0, n - 1                             # Set upper, bottom, left, and right bounds.
        while l < r and u < d:                                      # While the left bound < right and upper < bottom.
            ans.extend([matrix[u][j] for j in xrange(l, r)])        # extend along upper bound from left to right
            ans.extend([matrix[i][r] for i in xrange(u, d)])        # extend along right bound from upper to bottom
            ans.extend([matrix[d][j] for j in xrange(r, l, -1)])    # extend along bottom bound from right to left
            ans.extend([matrix[i][l] for i in xrange(d, u, -1)])    # extend along left bound from bottom to top
            u, d, l, r = u + 1, d - 1, l + 1, r - 1                 # upper = upper + 1, down = down - 1, left = left + 1, right = right - 1
        if l == r:                                                  # if left matches right, extend up and down
            ans.extend([matrix[i][r] for i in xrange(u, d + 1)])
        elif u == d:                                                # if upper matches down, extend left to right 
            ans.extend([matrix[u][j] for j in xrange(l, r + 1)])
        return ans
        
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        