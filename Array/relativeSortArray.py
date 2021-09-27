# https://leetcode.com/problems/relative-sort-array/
import collections
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        back = []
        front = []
        arr1_ct = collections.Counter(arr1)     # O(n) space and time
        
        for val in arr2:                        # O(m)
            front.extend([val]*arr1_ct.pop(val))
            
        for key in arr1_ct:
            back.extend([key] * arr1_ct[key])   # O(n-m)
            
        return front + sorted(back)             # O(n * log(n))
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        