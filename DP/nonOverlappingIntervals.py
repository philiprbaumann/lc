#https://leetcode.com/problems/non-overlapping-intervals/
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        erased = 0
        end = float("-inf")
        
        for i in sorted(intervals, key=lambda x: x[1]):
            if i[0] >= end:
                end = i[1]
            else:
                erased += 1    
        
        return erased 
        """
        :type intervals: List[List[int]]
        :rtype: int
        """