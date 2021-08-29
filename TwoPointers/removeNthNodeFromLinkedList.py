#https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while (fast.next):
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        