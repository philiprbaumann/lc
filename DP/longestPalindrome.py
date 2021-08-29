#https://leetcode.com/problems/longest-palindromic-substring/
class Solution(object):
    def longestPalindrome(self, s):
        max_pal = ""
        for i in range(0, len(s)):
            max_pal = max(max_pal, self.checkPalindrome(s, i, i), self.checkPalindrome(s, i, i+1), key=len )
        return max_pal
        """
        :type s: str
        :rtype: str
        """
        
    def checkPalindrome(self, s, l, r):
        while (l > -1 and r < len(s) and s[l] == s[r]):
            l-=1
            r+=1
        return s[l+1:r]