#https://leetcode.com/problems/implement-strstr/
class Solution(object):
    # This feels like a sliding window problem.
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        for i in range(0, len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        