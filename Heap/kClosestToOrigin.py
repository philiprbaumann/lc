# https://leetcode.com/problems/k-closest-points-to-origin/
# Solution is easy, but getting it efficient is harder
# First iteration:
import heapq
class Solution(object):
    def kClosest(self, points, k):
        minHeap = ans = []
        for p in points:
            heapq.heappush(minHeap, [((p[0]**2) + (p[1]**2) ) ** 0.5, p[0], p[1]])
            
        return [ [ x[1], x[2] ] for x in heapq.nsmallest(k, minHeap) ]
            
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

# Second iteration was a maxheap approach using heappushpop
# This one is much faster
import heapq
class Solution(object):
    def kClosest(self, points, k):
        maxHeap = []
        for p in points:
            eucl = ((p[0]**2) + (p[1]**2) ) ** 0.5
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, [-eucl, p[0], p[1]])
            else:
                heapq.heappushpop(maxHeap, [-eucl, p[0], p[1]])
 
        return [ [x[1],x[2]] for x in maxHeap ]
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        