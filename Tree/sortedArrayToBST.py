#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        return self.helper(nums, len(nums), 0)
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

    def helper(self, nums, upper, lower):
        if lower == upper:
            return None
        
        middle = (lower + upper) // 2
        
        node = TreeNode(nums[middle])
        node.left = self.helper(nums, middle, lower)
        node.right = self.helper(nums, upper, middle+1)
        
        return node