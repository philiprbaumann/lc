#https://leetcode.com/problems/sum-of-even-numbers-after-queries/
class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        # Close but slow
        # Lets cache the sums beforehand
        
        s = 0
        evens = []
        for num in nums:
            if num%2 == 0:
                s += num 
            
        for val, index in queries:
            if nums[index]%2 == 0: s -= nums[index]
            nums[index] += val
            if nums[index]%2 == 0: s += nums[index]
            evens.append(s)            
            
        return evens
        
        
        # Used to be odd, now is even => add new num[index]
        # Used to be even, now is even => add new val
        # Used to be odd, now is odd => no change
        # Used to be even, now is odd => subtract original