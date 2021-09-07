# https://leetcode.com/problems/lru-cache/

class Node(object):
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        """
        :type capacity: int
        """
        

    def get(self, key):
        if key in self.dict:
            node = self.dict[key]
            self.remove(node)
            self.add(node)
            return node.value
        return -1
               
        """
        :type key: int
        :rtype: int
        """
        

    def put(self, key, value):
        if key in self.dict:
            self.remove(self.dict[key])
        node = Node(key, value)
        self.dict[key] = node
        self.add(node)
        if len(self.dict) > self.capacity:
            n = self.head.next
            self.remove(n)
            del self.dict[n.key]
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        
    def add(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.prev = prev
        node.next = self.tail

        
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)