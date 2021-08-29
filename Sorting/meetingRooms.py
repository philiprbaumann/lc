#https://leetcode.com/problems/meeting-rooms/
class Solution(object):
    def canAttendMeetings(self, intervals):
        intervals = sorted(intervals)
        for x in range(1, len(intervals), 1):
            if intervals[x][0] < intervals[x-1][1]:
                return False 
        return True
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        