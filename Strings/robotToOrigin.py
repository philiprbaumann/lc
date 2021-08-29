# https://leetcode.com/problems/robot-return-to-origin/
class Solution(object):
    def judgeCircle(self, moves):
        vertical = 0
        horizontal = 0
        for move in moves:
            if move == "U":
                vertical+=1
            elif move == "D":
                vertical-=1
            elif move == "L":
                horizontal-=1
            elif move == "R":
                horizontal+=1
        return (vertical == 0 and horizontal == 0)
        """
        :type moves: str
        :rtype: bool
        """