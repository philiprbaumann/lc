# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        slow, fast = head, head
        
        # Find the midpoint.
        while (fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
        
        # Reverse from the midpoint
        prev, curr = None, slow.next
        while(curr):
            tmpnext = curr.next
            curr.next = prev
            prev = curr 
            curr = tmpnext
        slow.next = None
        
        # Merge
        head1 ,head2 = head, prev
        while head1 and head2:
            nxt1 = head1.next
            nxt2 = head2.next

            head1.next = head2
            head1 = nxt1

            head2.next = head1
            head2 = nxt2
             
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        