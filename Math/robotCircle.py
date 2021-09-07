# https://leetcode.com/problems/robot-bounded-in-circle/

class Solution(object):
    def isRobotBounded(self, instructions):
        x, y, dx, dy = 0, 0, 0, 1
        for char in instructions:
            if char == 'R': dx, dy = dy, -dx
            if char == 'L': dx, dy = -dy, dx
            if char == 'G': x, y = x + dx, y + dy
        return (x, y) == (0, 0) or (dx, dy) != (0,1)
        """
        :type instructions: str
        :rtype: bool
        """