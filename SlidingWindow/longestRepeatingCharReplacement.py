#https://leetcode.com/problems/longest-repeating-character-replacement/
class Solution(object):
    def characterReplacement(self, s, k):
        maxLen = maxCount = i = 0
        ct = defaultdict(int)
        
        while (i < len(s)):
            ct[s[i]] += 1
            
            maxCount = max(maxCount, ct[s[i]])
            
            if maxLen < maxCount + k:
                maxLen += 1
            else:
                ct[s[i-maxLen]] -= 1
            i += 1
        return maxLen
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        