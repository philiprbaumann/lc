# https://leetcode.com/problems/inorder-successor-in-bst
# My solution is in 96% off the top of my head. Works perfectly. 
class Solution(object):
    def inorderSuccessor(self, root, p):
        stack = []
        foundNode = False
        
        while (True):
            while (root):
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop()
                if foundNode:
                    return root
                if root == p:
                    foundNode = True
                root = root.right
            else:
                return None
           
        