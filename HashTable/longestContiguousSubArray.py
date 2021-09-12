# https://leetcode.com/problems/subarray-sum-equals-k
# Key things to remember:
#   1. Two pointer can't really work here given the negative numbers
#   2. Instead of iterating backwards to determine if a valid sum exists, we can use a hashMap to just check existance of the difference.
class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        numSum = 0
        d = defaultdict(int)
        d[0] = 1
        
        for i in range(len(nums)):
            numSum += nums[i]
            count += d[numSum-k]     # We are essentially using a hashMap to check if there exists a previous sum that adds to this difference that we can "subtract" from our contiguous array Sum.
            d[numSum] +=1                   # We increment the current sum by one, using get to make it a "defaultDict"
            
        return count
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        