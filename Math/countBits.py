#https://leetcode.com/problems/counting-bits/
class Solution(object):
    def countBits(self, n):
        counts = [0, 1]
        i = 1
        while (i < n+1):
            counts.extend(counts[i:i+i])
            counts.extend([x+1 for x in counts[i:i+i]])
            i *= 2
            
        return counts[:n+1]
        """
        :type n: int
        :rtype: List[int]
        """ 