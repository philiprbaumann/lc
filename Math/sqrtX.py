#https://leetcode.com/problems/sqrtx/
class Solution(object):
    def mySqrt(self, x):
        r = x                   
        while r*r > x:          
            r = (r + x/r) / 2
            #r = r - ((r**2 - x)/ 2*r)
        return r
        """
        :type x: int
        :rtype: int
        """
        