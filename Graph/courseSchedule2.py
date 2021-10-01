# https://leetcode.com/problems/course-schedule-ii
# This is a topological sort. Can be used in build systems.
# Keep track of visited nodes via three states in an array. 
# The graph is an adjacency hash. 
# Usually the order is reversed in a stack, but the course/prereq ordering of this question means its in the proper order. 
class Solution(object):
    def dfs(self, node):
        if self.visited[node] == -1: return False
        if self.visited[node] == 1: return True
        
        self.visited[node] = -1
        
        for x in self.graph[node]:
            if not self.dfs(x):
                return False
            
        self.visited[node] = 1
        self.ans.append(node)
        return True
        
        
    
    def findOrder(self, numCourses, prerequisites):
        self.graph = defaultdict(list)
        self.visited = [0 for _ in range(numCourses)]
        self.ans = []
        
        for course, prereq in prerequisites:
            self.graph[course].append(prereq)
                
        for x in range(numCourses):
            if not self.dfs(x):
                return []
        
        return self.ans
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        