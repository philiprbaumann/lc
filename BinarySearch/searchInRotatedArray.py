#https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution(object):
    # modified binary search
    def search(self, nums, target):
        if not nums:
            return -1
        
        low, high = 0, len(nums) -1 
        
        while (low <= high):
            middle = (low + high) // 2 
            
            if nums[middle] == target:
                return middle
            
            if nums[low] <= nums[middle]:
                if nums[low] <= target <= nums[middle]:
                    high = middle 
                else:
                    low = middle + 1
            else:
                if nums[middle] <= target <= nums[high]:
                    low = middle + 1
                else:
                    high = middle 
        return -1 
                
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        