#https://leetcode.com/problems/search-in-a-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        if root and root.val > val:
            root = self.searchBST(root.left, val)
        elif root and root.val < val:
            root = self.searchBST(root.right, val)
        return root
             
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        