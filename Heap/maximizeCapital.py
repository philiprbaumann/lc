# Remembering how to use heapq. I was pretty close to getting this one right off the bat,
# but I was overcomplicating the solution by attempting to heappop the rest of the 
# currProjects which are on the stack before I moved on with the newly gained capital.
# The trick here is realizing that you don't need to remove these projects given these are all 
# still viable projects which can be chosen to maximize profits.
import heapq
class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        projects = sorted(zip(capital, profits)) # Zip and reverse 
        currProjects = []
        for _ in range(k):
            while (projects and projects[0][0] <=  w):
                heapq.heappush(currProjects, -projects.pop(0)[1])
            if currProjects:
                w -= heapq.heappop(currProjects)
        return w