#https://leetcode.com/problems/subtree-of-another-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        def traverseTree(node):
            return "#" + str(node.val) + " " + traverseTree(node.left) + " " + traverseTree(node.right) if node else "$"
        
        return traverseTree(subRoot) in traverseTree(root)
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """