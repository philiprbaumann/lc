#https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if root:
            return max(self.maxDepth(root.right) + 1, self.maxDepth(root.left) + 1)
        else:
            return 0
        """
        :type root: TreeNode
        :rtype: int
        """
        