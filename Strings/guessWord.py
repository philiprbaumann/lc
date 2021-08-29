#https://leetcode.com/problems/guess-the-word/
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """
class Solution(object):
    def getMatch(self, word1, word2):
        count = 0
        for x,y in zip(word1, word2):
            if x == y:
                count += 1
        return count
    
    def findSecretWord(self, wordlist, master):
        i, matchCount =  0, 0
        while (i < 10 and matchCount != 6):
            index = random.randint(0,len(wordlist)-1)
            currentWord = wordlist[index]
            tmpCount = master.guess(currentWord)
            candidates = []
            for word in wordlist:
                if self.getMatch(word, currentWord) == tmpCount:
                    candidates.append(word)
            wordlist = candidates
            i += 1
        return currentWord    
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        