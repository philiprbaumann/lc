# Memoization!!! 
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

# Technically I think this works, but it's slow and stack heavy. Performs a lot of repeat actions too.
class Solution(object):
    def climbStairs(self, n):
        if n<1:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
        """
        :type n: int
        :rtype: int
        """
