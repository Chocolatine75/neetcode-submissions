class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        maxi = 0

        rows,cols = len(grid),len(grid[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(rows):
            for j in range(cols):

                if grid[i][j] != 1:
                    continue
                
                q = deque([(i,j)])
                currmax = 0
                grid[i][j] = 0

                while q:
                    x,y = q.popleft()
                    currmax +=1

                    for dx,dy in directions:
                        
                        if 0<= x+dx< rows and 0<= y+dy<cols and grid[x+dx][y+dy] == 1:
                            grid[x+dx][y+dy] = 0

                            q.append((x+dx,y+dy))
                if currmax >maxi:
                    maxi = currmax
        return maxi
            



        