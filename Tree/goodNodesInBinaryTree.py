# https://leetcode.com/problems/count-good-nodes-in-binary-tree
# The catch here is in the wording. It's not the _last_ node, but rather the MAXIMUM value node in the branch.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self, root, currMax):
        if root is None:
            return 0

        if root.val >= currMax:
            return 1 + self.helper(root.left, max(currMax, root.val)) + self.helper(root.right, max(currMax, root.val))
        else:
            return self.helper(root.left, max(currMax, root.val)) + self.helper(root.right, max(currMax, root.val))

    def goodNodes(self, root):
        return 1 + self.helper(root.left, root.val) + self.helper(root.right, root.val)
        """
        :type root: TreeNode
        :rtype: int
        """
        