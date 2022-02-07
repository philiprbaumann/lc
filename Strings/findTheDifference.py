# https://leetcode.com/problems/find-the-difference/
# Really easy. Can't use sets here because it removes duplicate so fails edge cases like "a"/"aa"
class Solution(object):
    def findTheDifference(self, s, t):
        if s is None:
            return t 
        s, t = list(s), list(t)
        s.sort()
        t.sort()
        for i,c in enumerate(t):
            if i == len(s) or c != s[i]:
                return c
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        