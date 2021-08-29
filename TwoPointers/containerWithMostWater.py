#https://leetcode.com/problems/container-with-most-water/
class Solution(object):
    def maxArea(self, height):
        i, j = 0, len(height)-1
        maxArea = 0
        while (i < j):
            maxArea = max(maxArea, min(height[i], height[j]) * (j-i))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
                
        return maxArea
        """
        :type height: List[int]
        :rtype: int
        """
        