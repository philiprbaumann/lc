#https://leetcode.com/problems/trapping-rain-water/
class Solution(object):
    def trap(self, height):
        maxLeftHeights = [0] * len(height)
        maxRightHeights = [0] * len(height)
        
        water, maxLeft, maxRight = 0, height[0], height[-1]
        
        for index in range(len(height)):
            maxLeft = max(maxLeft, height[index])
            maxLeftHeights[index] = maxLeft
            
        for index in range(len(height)-1, -1, -1):
            maxRight = max(maxRight, height[index])
            maxRightHeights[index] = maxRight  
        
        for x in range(len(height)):
            water += min(maxLeftHeights[x], maxRightHeights[x]) - height[x]
            
        return water