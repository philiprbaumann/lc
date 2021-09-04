# https://leetcode.com/problems/copy-list-with-random-pointer/
# The trick with this one is realizing that you can pass a lambda into a defaultdict to create an empty node object that you set later.
# This allows you to perform it in O(N) space and time vs. the O(2N) time and space version I originally came up with.
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        nodeMap = defaultdict(lambda: Node(-1))
        nodeMap[None] = None
        n = head

        while (n):
            nodeMap[n].val = n.val
            nodeMap[n].random = nodeMap[n.random]
            nodeMap[n].next = nodeMap[n.next]
            n = n.next

        return nodeMap.get(head)

# My original solution:
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        nodeMap = {None: None}
        n = m = head

        while (m):
            nodeMap[m] = Node(m.val)                        # Just creating the node objects to set later
            m = m.next

        while (n):
            nodeMap[n].next = nodeMap.get(n.next)           # Get because if it DNE it returns None
            nodeMap[n].random = nodeMap.get(n.random)
            n = n.next
            
        return nodeMap.get(n)                               # No need for root pointer because we have map.
        
        """
        :type head: Node
        :rtype: Node
        """
        