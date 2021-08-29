#https://leetcode.com/problems/climbing-stairs/
class Solution(object):
    def climbStairs(self, n):
        steps = [1, 2]
        for i in range(2, n):
            steps.append(steps[i-2] + steps[i-1])
        
        return steps[n-1]
        """
        :type n: int
        :rtype: int
        """
        