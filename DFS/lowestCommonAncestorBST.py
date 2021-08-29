#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object): 
    def lowestCommonAncestor(self, root, p, q):
        stack = [root]
        parents = {root: None}
        
        while p not in parents or q not in parents:
            node = stack.pop()
            
            if node.left:
                parents[node.left] = node
                stack.append(node.left)
            if node.right:
                parents[node.right] = node
                stack.append(node.right)
                
        ancestors = set([])
        
        while p:
            ancestors.add(p)
            p = parents[p]
            
        while q not in ancestors:
            q = parents[q]
            
        return q
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        