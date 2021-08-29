#https://leetcode.com/problems/path-sum-ii/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, root, targetSum, currentPath, paths):
        if root is None:
            return
        
        currentPath.append(root.val)
        
        if targetSum == root.val and not root.left and not root.right:
            paths.append(list(currentPath))
        else:
            self.dfs(root.left, targetSum - root.val, currentPath, paths)
            self.dfs(root.right, targetSum - root.val, currentPath, paths)
            
        currentPath.pop()


    def pathSum(self, root, targetSum):
        paths = []
        self.dfs(root, targetSum, [], paths)
        return paths
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        