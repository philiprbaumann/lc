# https://leetcode.com/problems/kth-largest-element-in-an-array/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        if inorder:
            root = preorder.pop(0)
            node = TreeNode(root)
            root_index = inorder.index(root)
            node.left = self.buildTree(preorder, inorder[:root_index])
            node.right = self.buildTree(preorder, inorder[root_index+1:])
            return node
        return None
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        