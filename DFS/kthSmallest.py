# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        stack = [root]
        while (stack):
            while (root):
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        