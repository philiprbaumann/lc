#https://leetcode.com/problems/top-k-frequent-elements/
import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        buckets = [ [] for _ in range(len(nums)+1) ]
        resp = []
        
        for num, freq in collections.Counter(nums).items():
            buckets[freq].append(num)
            
        for row in buckets[::-1]:
            if len(row): resp += row
            if len(resp) >= k: return resp[:k]
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        