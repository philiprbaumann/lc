#https://leetcode.com/problems/valid-anagram/
class Solution(object):
    def isAnagram(self, s, t):
        charCount = defaultdict(int)
        
        for char in s: charCount[char] += 1
        for char in t: charCount[char] -= 1
            
        return all(total == 0 for total in charCount.values())
        """
        :type s: str
        :type t: str
        :rtype: bool
        """