#https://leetcode.com/problems/asteroid-collision/
class Solution(object):
    def asteroidCollision(self, asteroids):
        s = []
        for i, a in enumerate(asteroids):
            if a < 0:
                while s and s[-1] > 0 and s[-1] < -a:
                    s.pop()
                if not s or s[-1] < 0:
                    s += a,
                elif s[-1] == -a:
                    s.pop()
            else:
                s += a,
        
        return s