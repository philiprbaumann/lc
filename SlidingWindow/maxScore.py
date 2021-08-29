#https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
class Solution(object):
    def maxScore(self, cardPoints, k):
        s = sum(cardPoints[:k])
        currMax = s
        for x in range(1, k+1):
            s += cardPoints[-x] - cardPoints[k-x]
            currMax = max(currMax, s)
        return currMax
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """