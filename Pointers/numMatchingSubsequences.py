#https://leetcode.com/problems/number-of-matching-subsequences/
class Solution(object):
    def numMatchingSubseq(self, s, words):
        d = defaultdict(list)
        
        for word in words:
            d[word[0]].append(iter(word[1:]))
            
        for char in s:
            for it in d.pop(char, ()):
                d[next(it, None)].append(it)
                
        return len(d[None])
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        