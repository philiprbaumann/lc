#https://leetcode.com/problems/is-subsequence/
class Solution(object):
    def isSubsequence(self, s, t):
        s = list(s)
        for char in t:
            if s and char == s[0]:
                s.pop(0)
            
        return len(s) == 0
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
    def isSubsequence(self, s, t):
        t = iter(t)
        return all(c in t for c in s)
# Just testing whether all characters in s are also in t (in order).
# Takes O(|s| + |t|) time and O(1) space.