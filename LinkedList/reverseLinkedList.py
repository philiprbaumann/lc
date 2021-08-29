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
            
            