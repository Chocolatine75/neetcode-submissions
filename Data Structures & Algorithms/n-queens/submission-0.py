class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for i in range(n)]

        def isValid(x,y,board):
            row = x-1
            while row >=0:
                if board[row][y] == "Q":
                    return False
                row -=1
            
            row,col = x-1,y-1
            while col >=0 and row>=0:

                if board[row][col] == 'Q':
                    return False
                row-=1
                col -=1

            row,col = x-1,y+1
            while row>=0 and n>col:

                if board[row][col] == 'Q':
                    return False
            
                row-=1
                col+=1
            return True

        def back(r):

            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                
            for c in range(n):
                if isValid(r,c,board):
                    board[r][c] = "Q"
                    back(r+1)
                    board[r][c] ="."
                
        back(0)
        return res
                    


         