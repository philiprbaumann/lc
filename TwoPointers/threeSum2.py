# https://leetcode.com/problems/3sum/
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        triplets = []
        for x in range(len(nums)-2):
            if x > 0 and nums[x] == nums[x-1]:
                continue
            low = x+1
            high = len(nums)-1
            while (low < high):
                if nums[low] + nums[high] > -nums[x]: 
                    high -= 1
                elif nums[low] + nums[high] < -nums[x]:
                    low += 1
                else:
                    triplets.append([nums[x], nums[low], nums[high]])
                    while (low < high and nums[low] == nums[low+1]):
                        low += 1
                    while (low < high and nums[high] == nums[high-1]):
                        high -= 1
                    low += 1
                    high -= 1
        return triplets