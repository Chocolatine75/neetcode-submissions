class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        row = len(grid)
        col = len(grid[0])
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        def bfs(r,c):
            q= deque()
            q.append((r,c))
            grid[r][c] = '0'

            while q:
                x,y = q.popleft()

                for dx,dy in directions:

                    ax,ay = dx+x,dy+y
                    if 0<=ax <row and 0<=ay<col and grid[ax][ay]=="1":
                        q.append((ax,ay))
                        grid[ax][ay] = "0"
        count = 0
        for r  in range(row):
            for c in range(col):

                if grid[r][c] == "1":
                    bfs(r,c)
                    count +=1
        return count




