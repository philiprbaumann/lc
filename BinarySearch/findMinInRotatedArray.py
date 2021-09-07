# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution(object):
    def findMin(self, nums):
        low, high = 0, len(nums)-1
        
        while (low < high):
            middle = (low + high) // 2
            if nums[middle] > nums[high]:
                low = middle + 1
            else:
                high = middle
        return nums[low]
# Runtime: 24 ms, faster than 85.36% of Python online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 13.8 MB, less than 26.98% of Python online submissions for Find Minimum in Rotated Sorted Array.
        
#         if nums[0] < nums[-1]:
#             return nums[0]
#         else:
#             return self.helper(nums)
            
#     def helper(self, nums):
#         if len(nums) == 1:
#             return nums[0]
#         if len(nums) == 2:
#             return min(nums[0], nums[1])
        
#         middle = len(nums) // 2
#         if nums[middle] > nums[-1]:
#             return self.helper(nums[middle:])
#         else:
#             return self.helper(nums[:middle+1])

# Runtime: 24 ms, faster than 85.36% of Python online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 13.6 MB, less than 82.50% of Python online submissions for Find Minimum in Rotated Sorted Array.
            