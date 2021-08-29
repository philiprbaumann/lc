#https://leetcode.com/problems/longest-string-chain/
class Solution(object):
    def longestStrChain(self, words):
        wordDict, largest = {}, 0
        
        words.sort(key=len)
        
        for word in words:
            wordDict[word] = 1
            
        for word in words:
            for i in range( len(word) ):
                pred = word[:i] + word[i+1:]
                if pred in wordDict:
                    wordDict[word] = max(wordDict[word], wordDict[pred] + 1)
            largest = max(wordDict[word], largest)
        return largest
        """
        :type words: List[str]
        :rtype: int
        """