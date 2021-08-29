#https://leetcode.com/problems/valid-palindrome/
class Solution(object):
    def isPalindrome(self, s):
        # Iterate with two pointers
        l = 0
        r = len(s) - 1
        s = s.lower()
        while l < r:
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            else:
                if s[l] != s[r]:
                    return False
                else:
                    l+=1
                    r-=1
        return True