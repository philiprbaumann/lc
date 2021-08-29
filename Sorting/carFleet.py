#https://leetcode.com/problems/car-fleet/
class Solution(object):
    def carFleet(self, target, position, speed):
        numFleets, currMax = 0, None
        for p, s in sorted(zip(position, speed), reverse=True):
            rdsLeft = (target - p) / float(s)
            if currMax is None or rdsLeft > currMax:
                numFleets += 1
                currMax = rdsLeft
        return numFleets 

        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """