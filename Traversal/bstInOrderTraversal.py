#https://leetcode.com/problems/binary-tree-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # In order traversal -> in = left, root, right
    def inorderTraversal(self, root):
        stack, order = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return order
            new_node = stack.pop()
            order.append(new_node.val)
            root = new_node.right
                