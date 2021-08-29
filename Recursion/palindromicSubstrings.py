#https://leetcode.com/problems/palindromic-substrings/
class Solution(object):
    def countHelper(self, s, lower, upper):
        ans = 0
        
        while (lower >= 0 and upper < len(s) and s[lower] == s[upper]):
            lower -= 1
            upper += 1
            ans += 1
            
        return ans
    
    def countSubstrings(self, s):
        total = 0
        
        for x in range(len(s)):
            total += self.countHelper(s, x, x) + self.countHelper(s, x, x+1)
            
        return total
        """
        :type s: str
        :rtype: int
        """
        