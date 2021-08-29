#https://leetcode.com/problems/pacific-atlantic-water-flow/
class Solution(object):
    def dfs(self, x, y, visited, heights, prevHeight):
        if x < 0 or y < 0 or x >= len(heights[0]) or y >= len(heights) or (y,x) in visited or heights[y][x] < prevHeight:
            return
        
        visited.add( (y,x) )

        return self.dfs(x-1, y, visited, heights, heights[y][x]) or self.dfs(x+1, y, visited, heights, heights[y][x]) or self.dfs(x, y+1, visited, heights, heights[y][x]) or self.dfs(x, y-1, visited, heights, heights[y][x])
            
        
    def pacificAtlantic(self, heights):
        rows, cols = len(heights), len(heights[0])
        atlPeaks, pacPeaks, ans = set([]), set([]), []

        # Atlantic search
        for x in range(cols):
            self.dfs(x, rows - 1, atlPeaks, heights, -1)
            self.dfs(x, 0, pacPeaks, heights, -1)
        for y in range(rows):
            self.dfs(cols-1, y, atlPeaks, heights, -1)
            self.dfs(0, y, pacPeaks,  heights, -1)

        return atlPeaks & pacPeaks


        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        


