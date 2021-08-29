#https://leetcode.com/problems/binary-tree-preorder-traversal/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # Pre order = root, left, right
    def preorderTraversal(self, root):
        stack, order = [root], []
        while stack:
            node = stack.pop()
            if node:
                order.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
            
        return order
        """
        :type root: TreeNode
        :rtype: List[int]
        """