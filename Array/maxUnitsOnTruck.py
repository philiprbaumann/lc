# https://leetcode.com/problems/maximum-units-on-a-truck/
# Solved this on my own, it was an easy.
# My approach created a new variable instead of just decreasing truckSize. 
# This is something I need to keep in mind. Updating existing values is always going to be more efficient than allocating
# a new variable and updating that one. 
class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key= lambda x: x[1], reverse=True)
        unitCount = 0
        
        for numBoxes, boxUnits in boxTypes:
            if truckSize > numBoxes:
                truckSize -= numBoxes
                unitCount += numBoxes * boxUnits
            else:
                unitCount += truckSize * boxUnits # Remember, even if we can't fit _all_ units, we want to fit as many as we can.
                break
        return unitCount 
    
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """