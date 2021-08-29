#https://leetcode.com/problems/single-number/
class Solution(object):
    def singleNumber(self, nums):
        res = 0
        for num in nums:
            nums[0] ^= num # XOR
        return res
    
        """
        :type nums: List[int]
        :rtype: int
        """

    def singleNumber(self, nums):
        numbers = {}
        for i in range(0, len(nums)):
            if numbers.has_key(nums[i]):
                del numbers[nums[i]]
            else:
                numbers[nums[i]] = 1
        return numbers.keys()[0]

        