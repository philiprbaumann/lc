# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum
class Solution(object):
    def numRollsToTarget(self, d, f, target):
        memo = {}
        
        def dp(d, target):
            if d == 0:
                if target > 0: return 0
                return 1
            
            if (d,target) in memo:
                return memo[(d,target)]
            
            to_return = 0

            for i in range( max(0, target-f), target):
                to_return += dp(d-1, i)
                    
            memo[(d,target)] = to_return
            
            return to_return
        
        return dp(d, target)%(10**9 + 7)
        
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        