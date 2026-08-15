class Solution:
    def dfs(self, grid, i, j):
        grid[i][j] = 0
        area = 0
        if i + 1 < len(grid) and grid[i + 1][j] == 1:
            area += self.dfs(grid, i + 1, j)
        if i - 1 > -1 and grid[i - 1][j] == 1:
            area += self.dfs(grid, i - 1, j)
        if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
            area += self.dfs(grid, i, j + 1)
        if j - 1 > -1 and grid[i][j - 1] == 1:
            area += self.dfs(grid, i, j - 1)
        return 1 + area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = self.dfs(grid, i, j)
                    if area > maxArea:
                        maxArea = area
        return maxArea