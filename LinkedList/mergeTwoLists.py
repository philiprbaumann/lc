#https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = node = ListNode(0)
        while (l1 and l2):
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
            
        node.next = l1 or l2
            
        return head.next 
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """