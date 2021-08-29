#https://leetcode.com/problems/missing-number/
class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        return (n * (n+1))/2 - sum(nums)
        """
        :type nums: List[int]
        :rtype: int
        """
        