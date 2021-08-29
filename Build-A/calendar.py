#https://leetcode.com/problems/my-calendar-i/
class Node:
    def __init__(self, s, e):
        self.s = s
        self.e = e
        self.left = None
        self.right = None
        
class MyCalendar(object):

    def __init__(self):
        self.root = None
        
    def search(self, node, s, e):
        if e <= node.s:
            if node.left:
                return self.search(node.left, s, e)
            else:
                node.left = Node(s,e)
                return True
        elif s >= node.e:
            if node.right:
                return self.search(node.right, s, e)
            else:
                node.right = Node(s,e)
                return True
        else: 
            return False
        
    def book(self, start, end):
        if self.root is None:
            self.root = Node(start,end)
            return True
        return self.search(self.root, start, end)
                  
        """
        :type start: int
        :type end: int
        :rtype: bool
        """

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)