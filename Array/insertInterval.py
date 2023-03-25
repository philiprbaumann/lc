# The trick here is thinking of it as three distinct segments which should be combined.
#https://leetcode.com/problems/insert-interval/
class Solution(object):
    def insert(self, intervals, newInterval):
        if len(intervals) == 0:
            return [newInterval]        
        start, end = newInterval[0], newInterval[1]
        left, right = [], []
        for interval in intervals:
            if interval[1] < start:
                left.append(interval)
            elif interval[0] > end:
                right.append(interval)
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])
        return left + [[start, end]] + right
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """