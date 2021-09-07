# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        if inorder:
            root = postorder.pop()
            node = TreeNode(root)
            rootIndex = inorder.index(root)
            node.right = self.buildTree(inorder[rootIndex+1:], postorder)
            node.left = self.buildTree(inorder[:rootIndex], postorder)
            return node
        return None
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        