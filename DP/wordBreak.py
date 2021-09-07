# https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]

# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         ok = [True]
#         words = set(wordDict)
        
#         for i in range(1, len(s)+1):
#             ok += any(ok[j] and s[j:i] in words for j in range(i)),
            
#         return ok[-1]

                
        