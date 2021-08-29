#https://leetcode.com/problems/koko-eating-bananas/
class Solution(object):
    def tryAnswer(self, piles, x):
        totalH = 0
        for pile in piles:
            totalH += ( (pile + (x - 1)) // x )
        return totalH
        
    def minEatingSpeed(self, piles, h):
        low, high = 1, max(piles)
        
        while (low <= high):
            middle = (low + high) // 2
            if self.tryAnswer(piles, middle) > h:
                low = middle + 1
            else:
                high = middle - 1
        return low
                
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """