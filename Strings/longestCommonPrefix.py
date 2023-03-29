class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        for char in strs[0]:
            prefix += char
            for s in strs:
                if s[:len(prefix)] != prefix:
                    return prefix[:-1]
        return prefix
            
            