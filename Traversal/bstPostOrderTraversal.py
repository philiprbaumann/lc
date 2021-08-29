#https://leetcode.com/problems/binary-tree-postorder-traversal/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # Post order = left, right, curr 
    def postorderTraversal(self, root):
        stack, order = [root], []
        while stack:
            node = stack.pop()
            if node:
                order.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return order[::-1]
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        