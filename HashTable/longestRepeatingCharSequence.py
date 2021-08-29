#https://leetcode.com/problems/longest-repeating-character-replacement/
class Solution(object):
    def characterReplacement(self, s, k):
        maxLen = maxCount = i = 0
        ct = defaultdict(int)
        
        while (i < len(s)):
            ct[s[i]] += 1                       # count[char] += 1
            
            maxCount = max(maxCount, ct[s[i]])  # is there a new maxCount?
            
            if maxLen < maxCount + k:           # if 0 < 1+2
                maxLen += 1                         # += 1
            else:
                ct[s[i-maxLen]] -= 1            # count of the first word in sequence subtract by one
            i += 1
        return maxLen
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        