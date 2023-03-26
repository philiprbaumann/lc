# The trick with this one is remembering to return last/prev and not current because current would be equal
# to the next of the last node ( which is null ).
#https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        last = None
        current = head
        while (current):
            next_node = current.next
            current.next = last
            last = current
            current = next_node
        return last
            
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head 
        while (curr):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            
        return prev
        """
        :type head: ListNode
        :rtype: ListNode
        """