# This is the optimal O(N) approach which leverages the fact that every move is a valid move to just keep "scores" of each possible winning pattern.
# If a person fills that entire pattern, then its value hits self.n or -self.n and it completes.
# VALID moves only is the key here. 
class TicTacToe(object):

    def __init__(self, n):
        self.row = [0] * n
        self.col = [0] * n
        self.diag = 0
        self.rdiag = 0
        self.n = n
        
        """
        Initialize your data structure here.
        :type n: int
        """
        

    def move(self, row, col, player):
        offset = 1 if player == 1 else -1
        
        self.row[row] += offset
        self.col[col] += offset
        
        if row == col: self.diag += offset
        if row == self.n -1 - col: self.rdiag += offset
                        
        if self.n in self.row or -self.n in self.row: return player
        if self.n in self.col or -self.n in self.col: return player
        if self.diag == self.n or self.diag == -self.n: return player
        if self.rdiag == self.n or self.rdiag == -self.n: return player
        
        return 0
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

# This is an O(N^2) implementation and isn't ideal. We know that every move is valid so lets use this to our advantage.
class TicTacToe(object):

    def __init__(self, n):
        self.board = [ [0 for _ in range(n)] for _ in range(n)]
        self.n = n
        
        """
        Initialize your data structure here.
        :type n: int
        """
        
        
    def checkWin(self, player):
        # Check horizontal
        for row in self.board:
            if row[0] != 0 and row.count(row[0]) == self.n:
                return player
            
        for col in range(self.n):
            for i in range(self.n):
                if self.board[i][col] == 0 or self.board[i][col] != self.board[0][col]:
                    break
            else: return player

        for i in range(self.n):
            if self.board[i][i] == 0 or self.board[i][i] != self.board[0][0]:
                break
        else: return player
        
        for r,c in zip(range(self.n-1, -1, -1), range(self.n)):
            if self.board[r][c] == 0 or self.board[r][c] != self.board[self.n-1][0]:
                break
        else: return player
        
        
        return 0
    
    
    def move(self, row, col, player):
        self.board[row][col] = player
        return self.checkWin(player)
        
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)