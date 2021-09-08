# https://leetcode.com/problems/find-the-celebrity
class Solution(object):
    def findCelebrity(self, n):
        possibleCelebrity = 0
        
        # Find Celebrity. 
        for x in range(1, n):
            if knows(possibleCelebrity, x):
                possibleCelebrity = x
            
        # Check if they know anyone that was already visited.
        for y in range(possibleCelebrity-1, -1, -1):
            if knows(possibleCelebrity, y):
                return -1 
            
        # Check if anyone doesn't know them. 
        for i in range(n):
            if not knows(i, possibleCelebrity):
                return -1 
            
        return possibleCelebrity