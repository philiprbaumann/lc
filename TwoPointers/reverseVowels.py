#https://leetcode.com/problems/reverse-vowels-of-a-string/submissions/
class Solution(object):
    def reverseVowels(self, s):
        start, end, s = 0, len(s) - 1, list(s)
        vowels = set('AEIOUaeiou')
        
        while (start <= end):
            while start <= end and s[start] not in vowels:
                start += 1
            while start <= end and s[end] not in vowels:
                end -= 1
            if start > end: break
            if s[start] in vowels and s[end] in vowels:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
                
        return ''.join(s)
        """
        :type s: str
        :rtype: str
        """