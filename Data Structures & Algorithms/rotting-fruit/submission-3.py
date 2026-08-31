class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        time = 0
        row = len(grid)
        col = len(grid[0])
        for  i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i,j))

                if grid[i][j] == 1:
                    fresh += 1
              
        
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        while fresh >0 and q:
            length = len(q)
            for i in range(length):
                rot = q.popleft()

                for a,b in directions:
                    r,c = rot[0]+a,rot[1]+b
                    if 0<=r< row and 0<=c< col and grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh -= 1
                        q.append((r,c))
            time+=1

        if fresh==0:
            return time
        return -1




