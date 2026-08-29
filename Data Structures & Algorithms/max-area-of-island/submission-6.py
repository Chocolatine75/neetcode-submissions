class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        lx=len(grid)
        ly=len(grid[0])

        def aux(x,y,l):
            grid[x][y]= 0
            if x-1>=0 and grid[x-1][y] == 1:
                l= aux(x-1,y,l) 
            if y-1>=0 and grid[x][y-1] == 1:
                l= aux(x,y-1,l)
            if x+1 < lx and grid[x+1][y]==1:
                l= aux(x+1,y,l) 
            if y+1 < ly and grid[x][y+1] == 1:
                l= aux(x,y+1,l)
            return l+1
        maxlen =0
        
        for x in range(lx):
            for y in range(ly):
                if grid[x][y]==1:
                    length = aux(x,y,0)
                    maxlen=max(maxlen,length)
        return maxlen


            
        