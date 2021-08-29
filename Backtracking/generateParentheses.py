#https://leetcode.com/problems/generate-parentheses
class Solution(object):
    def dfs(self, leftR, rightR, s, rsp):
        if leftR > rightR or leftR < 0 or rightR < 0:
            return      # This is also backtracking.
        if leftR==0 and rightR==0:
            rsp.append(s)
            return
        self.dfs(leftR-1, rightR, s+"(", rsp)
        self.dfs(leftR, rightR-1, s+")", rsp)
        
    def generateParenthesis(self, n):
        rsp = []
        self.dfs(n, n, '', rsp)
        return rsp
        """
        :type n: int
        :rtype: List[str]
        """
        