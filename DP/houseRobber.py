# https://leetcode.com/problems/house-robber/
class Solution(object):
    def rob(self, nums):
        maxSums = []
        for i, num in enumerate(nums):
            if (i-2)>0:
                maxSums.append(max(num + maxSums[i-2], num + maxSums[i-3]))
            elif (i-1) > 0:
                maxSums.append(num + maxSums[i-2])
            else:
                maxSums.append(num)
        if len(maxSums) == 1:
            return maxSums[0]
        return max(maxSums[-1], maxSums[-2])
        """
        :type nums: List[int]
        :rtype: int
        """