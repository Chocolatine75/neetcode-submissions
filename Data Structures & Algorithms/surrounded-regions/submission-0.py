class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(0,1),(0,-1),(-1,0),(1,0)]

        rows,col = len(board),len(board[0])

        def bfs():

            q= deque()

            for r in range(rows):
                for c in range(col):
                    if (r == 0 or r == rows-1 or c == 0 or c == col-1) and board[r][c] == 'O':
                        q.append((r,c))
            
            while q:
                x,y = q.popleft()

                if board[x][y] == 'O':
                    board[x][y] = 'V'
                    for dx,dy in directions:
                        if  0<= dx+x <rows and 0<= dy+y<col:
                            q.append((dx+x,dy+y))
        bfs()
        for i in range(rows):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                
                if board[i][j] == 'V':
                    board[i][j]='O'
                


        
        