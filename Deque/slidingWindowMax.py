# https://leetcode.com/problems/sliding-window-maximum
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        d = collections.deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] <= n:        # remove elements in dequeue outside of window
                d.pop()
            d.append(i)                         # Add num element to deque
            if d[0] == i - k:                   # if first element == currentIndex - k : outside of window therefore remove
                d.popleft()
            if i >= k - 1:
                out += nums[d[0]],
        return out


# import heapq
# class Solution(object):
#     def maxSlidingWindow(self, nums, k):
#         i = 0
#         ans = []
#         while (i + k <= len(nums)):
#             mHeap = [-x for x in nums[i:i+k]]
#             heapq.heapify(mHeap)
#             i += 1
#             ans.append(-mHeap[0])
#         return ans
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
        
        
# class Solution(object):
#     def maxSlidingWindow(self, nums, k):
#         i = 0
#         ans = []
#         while (i + k <= len(nums)):
#             ans.append(max(nums[i:i+k]))
#             i += 1
#         return ans
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """