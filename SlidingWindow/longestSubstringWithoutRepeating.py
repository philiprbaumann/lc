#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_len, start, alph_dict = 0, 0, {}
        for i, char in enumerate(s):
            if char in alph_dict and start <= alph_dict[char]: # If exists in dict and start is less than alph index
                start = alph_dict[char] + 1
            else:
                max_len = max(max_len, i - start + 1 )
            alph_dict[char] = i
        
        return max_len
        """
        :type s: str
        :rtype: int
        """