class Solution(object):
    def longestConsecutive(self, nums):
        nums = set(nums)
        maxLength = 0
        
        for num in nums:
            if num - 1 not in nums:
                x = num + 1
                while x in nums: 
                    x += 1
                maxLength = max(maxLength, x - num)
        
        return maxLength