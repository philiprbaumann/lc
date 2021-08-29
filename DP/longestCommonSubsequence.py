#https://leetcode.com/problems/longest-common-subsequence/
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        dp = [ [0 for x in range(len(text1)+1) ] for y in range(len(text2)+1) ]
        
        for i in range(1, len(text2)+1):
            found = 0
            for j in range(1, len(text1) + 1):
                if text2[i-1] == text1[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1     # if eql, take from last and add one
                else:
                    dp[i][j] = max( dp[i-1][j], dp[i][j-1] )
                    
        return dp[len(text2)][len(text1)]
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """