#https://leetcode.com/problems/delete-and-earn/
# We first transform the nums array into a points array that sums up the total num of points for that particular value. 
# A value of x will be assigned to index x in points.

# Version of house robber.
# nums: [2, 2, 3, 3, 3, 4] (2 appears 2 times, 3 appears 3 times, 4 appears once)
# points: [0, 0, 4, 9, 4] <- This is the gold in each house!

class Solution:
    def deleteAndEarn(self, nums):
        A = [0] * (max(nums or [0]) + 1)
        for i in nums:
            A[i] += i
        pre, cur = 0, 0
        for i in A:
            pre, cur = cur, max(cur, pre + i)
        return cur
        """
        :type nums: List[int]
        :rtype: int
        """
        