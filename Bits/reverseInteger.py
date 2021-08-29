#https://leetcode.com/problems/reverse-integer/
class Solution(object):
    def reverse(self, x):
        s = [-1, 1][x > 0]
        r = s * int(str(abs(x))[::-1])
        if -2**31 <= r <= 2**31: return r
        return 0
        """
        :type x: int
        :rtype: int
        """
        