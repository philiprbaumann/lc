# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # Find middle with turtle/hare.
        slow, fast, i = head, head, 0
        while (fast):
            i += 1
            fast = fast.next
            if (i%2==0 and fast):
                slow = slow.next

        # Reverse back half. 
        curr = slow
        prev = None
        while (curr):
            tmp = curr.next
            curr.next = prev 
            prev = curr
            curr = tmp

        # Merge lists.
        curr = head
        curr2 = prev
        while (curr):
            tmp = curr.next
            tmp2 = curr2.next
            curr.next = curr2
            curr2.next = tmp 
            curr = tmp
            curr2 = tmp2

        return head