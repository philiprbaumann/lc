#https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        verticalCuts.sort()
        horizontalCuts.sort()
        last, maxW, maxV = 0, 0, 0
        for cut in horizontalCuts:
            maxV = max(maxV, cut-last)
            last = cut
        maxV = max(maxV, h-last)
        
        last = 0
        for cut in verticalCuts:
            maxW = max(maxW, cut-last)
            last = cut
        maxW = max(maxW, w-last)
        
        return (maxW * maxV)%1000000007
                
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        