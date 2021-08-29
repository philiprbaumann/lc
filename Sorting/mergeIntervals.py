#https://leetcode.com/problems/merge-intervals/
class Solution(object):
    def canJump(self, nums):
        # If I have a preceding index idx in nums which has jump count jump which satisfies idx+jump >= last_position, I know that this idx is good enough to be treated as the last index because all I need to do now is to get to that idx. I am going to treat this new idx as a new last_position.
        last, i = len(nums)-1, len(nums)-1
        while (last != 0 and i != 0):
            i-=1
            if i + nums[i] >= last:
                last = i
            
        return (last == 0) 
        """
        :type nums: List[int]
        :rtype: bool
        """