class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height , width = len(grid), len(grid[0])
        maxArea = 0
        def dfs(r,c):
            if(r <0  or c < 0 or r > height -1 or c > width -1 or grid[r][c] == 0):
                return 0
            grid[r][c] = 0
            left = dfs(r,c-1)
            right = dfs(r,c+1)
            up = dfs(r+1,c)
            down = dfs(r-1,c)
            return 1 +left+right+down+up
        for r in range(height):
            for c in range(width):
                cur_area = dfs(r,c)
                if cur_area > maxArea:
                    maxArea = cur_area
        return maxArea
