#https://leetcode.com/problems/balance-a-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        order = self.inOrderTraversal(root)
        return self.convertBST(order, 0, len(order))
    
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
    # L, Curr, R
    def inOrderTraversal(self, root):
        stack, order = [], []
        while (True):
            while(root):
                stack.append(root)
                root = root.left
            if not stack:
                return order
            node = stack.pop()
            order.append(node.val)
            root = node.right 
            
    def convertBST(self, order, lower, upper):
        if lower == upper:
            return None
        
        middle = (lower + upper) // 2
        
        node = TreeNode(order[middle])
        node.left = self.convertBST(order, lower, middle)
        node.right = self.convertBST(order, middle+1, upper)
        return node