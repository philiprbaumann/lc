#https://leetcode.com/problems/unique-paths/
import math
class Solution(object):
    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1
        cn = max(m, n)
        ck = min(m, n)
        cn -= 1
        ck -= 1
        # From all possible steps (which is n-1 * m-1), divide by redundancies which are (n-1! and m-1!)
        return math.factorial(cn+ck) / (math.factorial(cn) * math.factorial(ck))
        """
        :type m: int
        :type n: int
        :rtype: int
        """