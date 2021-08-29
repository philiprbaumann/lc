#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        a, b = sorted([p.val, q.val])
        while not (a <= root.val <= b):
            if root.val > b:
                root = root.left
            else:
                root = root.right
            
        return root
                
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """