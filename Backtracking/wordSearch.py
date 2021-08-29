#https://leetcode.com/problems/word-search/
class Solution(object):
    def exist(self, board, word):
        if not board or not word:
            return False
        
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if self.dfs(board, i, j, word, 0):
                    return True
                
    def dfs(self, board, i, j, word, char_num):
        if char_num == len(word):
            return True
        
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
            return False
        
        if word[char_num] != board[i][j]:
            return False
        
        temp_char = board[i][j]
        board[i][j] = "#"
        
        
        response = self.dfs(board, i+1, j, word, char_num+1) \
                    or self.dfs(board, i-1, j, word, char_num+1) \
                    or self.dfs(board, i, j+1, word, char_num+1) \
                    or self.dfs(board, i, j-1, word, char_num+1)
           
        if not response:
            board[i][j] = temp_char
        
        return response
        