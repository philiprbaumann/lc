#https://leetcode.com/problems/max-area-of-island/
class Solution(object):
    def dfs(self, grid, x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0 or grid[x][y] == "#":
            return 0
        else:
            grid[x][y] = "#"
            return 1 + self.dfs(grid, x + 1, y) + self.dfs(grid, x - 1, y) + self.dfs(grid, x, y+1) + self.dfs(grid, x, y-1)
    
    def maxAreaOfIsland(self, grid):
        maxSum = 0
        for x in range( len(grid) ):
            for y in range( len(grid[0]) ):
                if grid[x][y] == 1:
                    maxSum = max(maxSum, self.dfs(grid, x, y,))
        return maxSum
        """
        :type grid: List[List[int]]
        :rtype: int
        """