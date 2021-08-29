#https://leetcode.com/problems/number-of-1-bits/
# Hamming Weight - the number of symbols that are different from the zero-symbol of the alphabet used
class Solution(object):
    def hammingWeight(self, n):
        ans = 0
        for x in range(32):
            if n & 1:
                ans += 1
            n >>= 1
        return ans
        """
        :type n: int
        :rtype: int
        """