# https://leetcode.com/problems/coin-change/
class Solution(object):
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        
        visited = {0}
        queue = [(0,0)]
        
        while (queue):
            curr, step = queue.pop(0)
            if curr == amount: return step
            
            for coin in coins:
                if curr + coin not in visited and curr + coin <= amount:
                    queue.append( (curr + coin, step + 1) )
                    visited.add(curr + coin)
                
        return -1
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """