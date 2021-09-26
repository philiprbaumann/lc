# https://leetcode.com/problems/sliding-window-maximum
# Turns out there's a thing called Monotonic queues. Pretty neat stuff. 
#       - O(1) push / O(1) pop / O(1) max
#       - takes O(n) to process list n -> performs better than heap implementation below  O(N * log(n) ) bc log(n) insertion time on heap
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        deque = collections.deque()
        rsp = []
        
        for i, n in enumerate(nums):
            if deque and deque[0] < i-k+1: deque.popleft()  # remove the any index values on the LEFT SIDE which are no longer in window
            while deque and nums[deque[-1]] < n:            # remove any index values on the RIGHT SIDE which are less than my new value
                deque.pop()
            deque.append(i)                                 # add new value index
            if i >= k - 1:                                  # if we've achieved the minimum window length index, then we can start adding to answer
                rsp.append(nums[deque[0]])
        
        return rsp

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