#https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/
class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        # Iterate with a pointer at i and i+m and see if they match as you go
        # good pattern trick
        streak = 0
        for i in range(len(arr)-m):
            streak = streak + 1 if arr[i] == arr[i+m] else 0
            if streak == (k-1)*m: return True
        return False