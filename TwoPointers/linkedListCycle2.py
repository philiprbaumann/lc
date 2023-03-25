# This approach works, but overcomplicates it. The first approach is preferable and cleaner. Given slow will never be null if fast isn't, we don't have to check fast too. 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head
        while (slow and fast and slow.next and fast.next and fast.next.next):
            if slow.next == fast.next.next:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
        """
        :type head: ListNode
        :rtype: bool
        """