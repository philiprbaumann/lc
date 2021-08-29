#https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        self.max = None
        self.helper(root)
        return self.max

    def helper(self, root):
        if root is None:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        self.max = max(self.max, left + root.val + right)
        
        return max(root.val + max(left, right), 0)
    
        """
        :type root: TreeNode
        :rtype: int
        """