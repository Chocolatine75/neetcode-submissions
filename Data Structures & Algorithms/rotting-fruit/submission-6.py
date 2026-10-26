class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        row = len(grid)
        col = len(grid[0])

        fresh =  0
        q = deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c] ==1:
                    fresh +=1
                
                if grid[r][c]== 2:
                    q.append((r,c,0))
        res = 0
        t = 0
        while q:
            x,y,t = q.popleft()

            for dx,dy in directions:

                ax,ay = dx+x,dy+y
                if 0<=ax<row and 0<=ay<col and grid[ax][ay] ==1:
                    grid[ax][ay] =2
                    q.append((ax,ay,t+1))
                    fresh -=1

        if fresh>0:
            return -1
        return t



            