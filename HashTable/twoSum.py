#https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i in range(0, len(nums)):
            if (target - nums[i]) in d:
                return [ d[target - nums[i]], i]
            else:
                d[ nums[i] ] = i
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        