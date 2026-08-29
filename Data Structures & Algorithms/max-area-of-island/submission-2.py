class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def aux(x,y,l):
            grid[x][y]= 0
            if x-1>=0 and grid[x-1][y] == 1:
                l= aux(x-1,y,l) 
            if y-1>=0 and grid[x][y-1] == 1:
                l= aux(x,y-1,l)
            if x+1 < len(grid) and grid[x+1][y]==1:
                l= aux(x+1,y,l) 
            if y+1 < len(grid[0]) and grid[x][y+1] == 1:
                l= aux(x,y+1,l)
            return l+1
        maxlen =0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]==1:
                    length = aux(x,y,0)
                    if maxlen < length:
                        maxlen = length
        return maxlen


            
        