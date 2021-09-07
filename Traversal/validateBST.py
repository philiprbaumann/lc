# https://leetcode.com/problems/validate-binary-search-tree/

class Solution:
    def isValidBST(self, root):
        stack, prev = [], float("-inf")

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right

        return True