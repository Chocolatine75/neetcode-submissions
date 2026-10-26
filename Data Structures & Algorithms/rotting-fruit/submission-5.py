class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])
        q = deque()
        fresh_fruit = 0
        for i in range(row):
            for j in range(col):
                
                if grid[i][j] == 2:
                    q.append((i,j,0))
                
                if grid[i][j] == 1:
                    fresh_fruit +=1
        directions = ((0,1),(1,0),(-1,0),(0,-1))
        last_time = 0
        while q :
            x,y,last_time = q.popleft()

            

            for dx,dy in directions:

                if 0<= x+dx<row and 0<= y+dy<col and grid[x+dx][y+dy] == 1:
                    grid[x+dx][y+dy] = 2
                    q.append((x+dx,y+dy,last_time+1))
                    fresh_fruit -=1
        if fresh_fruit>0:
            return -1

        return last_time
       
            

        