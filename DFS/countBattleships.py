# This works, but isn't the most efficient. I believe there's a way to do this mathematically.
class Solution(object):
    def countBattleships(self, board):
        shipCount = 0
        
        for i in range(len(board[0])):          # col
            for j in range(len(board)):         # row
                if board[j][i] == 'X':
                    shipCount += 1
                    board[j][i] = '*'
                    for xi, yj in [(-1,0), (1, 0), (0, 1), (0, -1)]:
                        ti, tj = i + xi, j + yj
                        while (ti >= 0 and tj >= 0 and ti < len(board[0]) and tj < len(board) and board[tj][ti] == 'X'):
                            board[tj][ti] = '*'
                            ti += xi
                            tj += yj
                        if ti != i + xi or tj != j + yj: break
        return shipCount

# This also works, but its less efficient and uses math:
class Solution(object):
    def countBattleships(self, board):
        shipCount = 0
        lengthCount = 0
        oneCount = 0
        
        for row in board:
            slow = 0
            fast = 0
            while (slow < len(row)):
                if row[slow] == 'X':
                    while (fast < len(row) and row[fast] == 'X'):
                        fast += 1
                    if slow+1 == fast: oneCount += 1
                    else: shipCount += 1
                    slow = fast
                else:
                    slow += 1
                    fast = slow
        for col in range(len(board[0])):
            slow = 0
            fast = 0
            while (slow < len(board)):
                if board[slow][col] == 'X':
                    while (fast < len(board) and board[fast][col] == 'X'):
                        fast += 1
                    if slow+1 != fast:
                        shipCount += 1
                        lengthCount += (fast - slow)
                    slow = fast
                else:
                    slow += 1
                    fast = slow
        return shipCount + (oneCount-lengthCount)
        """
        :type board: List[List[str]]
        :rtype: int
        """

# The best solution is actually searching for the "top-left-X" of every battleship. The question thread for getting to here:
#       1. How can I find both vertical and horizontal ships on one iteration?
#       2. What do vertical and horizontal ships have in common for counting that will still avoid overlapping?
#       3. They have a top-left corner of their ship. This ship will either be on the edge of the map or be surrounded by ocean.
class Solution(object):
    def countBattleships(self, board):
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X' and (i==0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1]=='.'):
                    count += 1
        return count

