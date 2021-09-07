# https://leetcode.com/problems/number-of-islands/
class Solution(object):
    def dfs(self, grid, i, j):
        if i > len(grid)-1 or j > len(grid[0])-1 or i < 0 or j < 0:
            return
        if grid[i][j] != "1":
            return
        grid[i][j] = "#"
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        
        
    def numIslands(self, grid):
        if not grid:
            return 0
        
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count+= 1
                    
        return count
    
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        