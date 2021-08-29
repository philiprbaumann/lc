#https://leetcode.com/problems/product-of-array-except-self/
class Solution(object):
    def productExceptSelf(self, nums):
        p = 1
        products = []
        
        for num in nums:
            products.append(p)
            p *= num
            
        p = 1
        for i in range(len(nums)-1, -1, -1):
            products[i] *= p
            p *= nums[i]
            
        return products
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        