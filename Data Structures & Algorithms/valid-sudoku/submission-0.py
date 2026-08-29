class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      
        for row in board:
            rset = set()
            for elt in row:
                if elt == '.':
                    continue
                elif elt in rset:
                    return False
                else:
                    rset.add(elt)
        
        for i in range(9):
            cset = set()
            for j in range(9):
                if board[j][i] == '.':
                    continue
                elif board[j][i] in cset:
                    return False
                else:
                    cset.add(board[j][i])
        for square in range(9):
            sset = set()

            for i in range(3):
                for j in range(3):
                    r = (square//3) * 3 + i
                    c = (square % 3) * 3 + j

                    if board[r][c] == '.':
                        continue
                    elif board[r][c] in sset:
                        return False
                    else:
                        sset.add(board[r][c])
        return True


                
                    


        