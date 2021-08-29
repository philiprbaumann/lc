#https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        root = n = ListNode(0)
        overflow = 0
        while (l1 or l2 or overflow):
            total = 0
            if l1 is not None:
                total += l1.val     
                l1 = l1.next
            if l2 is not None:
                total += l2.val
                l2 = l2.next
            total += overflow
            overflow = total // 10
            n.next = ListNode(total%10)
            n = n.next
            
        return root.next
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """