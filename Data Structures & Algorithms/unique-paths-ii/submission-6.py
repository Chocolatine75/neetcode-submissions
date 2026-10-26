class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = {(row - 1, col - 1): 1}

        def dfs(x, y):
            if x == row or y == col or grid[x][y] == 1:
                return 0

            if (x, y) in dp:

                return dp[(x, y)]
            dp[(x, y)] = dfs(x + 1, y) + dfs(x, y + 1)
            return dp[(x, y)]

        return dfs(0, 0)
        