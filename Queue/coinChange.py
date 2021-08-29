#https://leetcode.com/problems/coin-change/
class Solution(object):
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        
        queue = [(0,0)] # coin, amount
        visited = {0}
        
        for node, step in queue:
            for coin in coins:
                if (coin + node) in visited:
                    continue
                elif (coin + node) == amount:
                    return step + 1
                elif (coin + node) < amount:
                    queue.append( (coin+node, step+1) )
                    visited.add(coin + node)
                    
        return -1
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        