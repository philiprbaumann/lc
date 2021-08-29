#https://leetcode.com/problems/group-anagrams
class Solution(object):
    def groupAnagrams(self, strs):
        if len(strs) == 1:
            return [strs]
        prodOfAnagrams = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            prodOfAnagrams[sortedS] += [s]
        
        return prodOfAnagrams.values()
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        