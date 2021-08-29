# https://leetcode.com/problems/3sum/
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        three_set = []
        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: # if nums[1] == nums[2]
                continue 
            l = i+1
            r = len(nums)-1
            while (l < r):
                s = nums[l] + nums[r] + nums[i]
                if s > 0 :
                    r -=1 
                elif s < 0:
                    l += 1
                else:
                    three_set.append((nums[l], nums[r], nums[i]))
                    while l < r and nums[l] == nums[l+1]: # because its sorted, we remove duplicates by continuing to iterate, same below
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return three_set
            
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        