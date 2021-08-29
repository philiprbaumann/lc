#https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        lvlarr = []
        self.helper(root,lvlarr, 0)
        return lvlarr
    
    def helper(self, root, lvlarr, i):
        if root is None:
            return
        if i > len(lvlarr) - 1:
            lvlarr.append([root.val])
        else:
            lvlarr[i].append(root.val)
        
        i+=1
        if root.left:
            self.helper(root.left, lvlarr, i)
        if root.right:
            self.helper(root.right, lvlarr, i)