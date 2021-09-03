#https://leetcode.com/problems/find-median-from-data-stream/submissions/
# The trick with this one is to ALWAYS be push/popping instead of just pushing.
# Pushpop lets us retain a sorted nature to both heaps.
import heapq
class MedianFinder(object):

    def __init__(self):
        self.top = []
        self.bot = []
        

    def addNum(self, num):
        if len(self.top) == len(self.bot):
            heapq.heappush(self.top, -heapq.heappushpop(self.bot, -num))        # Heappushpop is faster
        else:
            heapq.heapush(self.bot, -heapq.heappushpop(self.top, num))          # Same here 
        """
        :type num: int
        :rtype: None
        """
        

    def findMedian(self):
        if (len(self.top) + len(self.bot))%2 == 0:
            return (self.top[0] - self.bot[0]) / 2.0                # Negative because self.bot is a maxHeap
        else:
            return self.top[0]
        """
        :rtype: float
        """
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()