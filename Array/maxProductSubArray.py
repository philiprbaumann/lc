#https://leetcode.com/problems/maximum-product-subarray/
class Solution(object):
    def maxProduct(self, nums):
        currentProd, currMax = 1, float("-inf")
        
        for num in nums:
            currentProd *= num
            currMax = max(currMax, currentProd)
            if num == 0:
                currentProd = 1
            
        currentProd = 1
        for i in range(len(nums)-1, -1, -1):
            currentProd *= nums[i]
            currMax = max(currMax, currentProd)
            if nums[i] == 0:
                currentProd = 1

        return currMax
        """
        :type nums: List[int]
        :rtype: int
        """