#https://leetcode.com/problems/insert-delete-getrandom-o1/
import random
class RandomizedSet(object):

    def __init__(self):
        self.lst = []
        self.setPos = {}
        """
        Initialize your data structure here.
        """
        

    def insert(self, val):
        if val in self.setPos:
            return False
        else:
            self.lst.append(val)
            self.setPos[val] = len(self.lst)-1
            return True 
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        

    def remove(self, val):
        if val in self.setPos:
            idx = self.setPos[val]
            last = self.lst[-1]
            self.lst[idx] = last
            self.setPos[last] = idx
            self.lst.pop()
            del self.setPos[val]
            return True
        else:
            return False
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        

    def getRandom(self):
        return random.choice(self.lst)
        
        """
        Get a random element from the set.
        :rtype: int
        """
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()