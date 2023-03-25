# https://leetcode.com/problems/happy-number/
# Used recursion and a set to track visited numbers. There's other approaches which can be used here too to prevent stack overuse.

class Solution(object):
    def isHappyR(self, n, visited):
        if n in visited:
            return False
        if sum([int(d)*int(d) for d in str(n)]) == 1:
            return True
        visited.add(n)
        return self.isHappyR(sum([int(d)*int(d) for d in str(n)]), visited)

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.isHappyR(n, set([]))

# There is an approach here that can use turtle/hare so you can avoid recursion. A little more complex, but isn't stack heavy.
# Floyd's Cycle-Finding Algorithm.
class Solution(object):
	def isHappy(self, n):
		#20 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 > 42 -> 20 
		#21 -> 5 -> 25 -> 29 -> 85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 ... cycle begins 
		slow = self.squared(n)
		fast = self.squared(self.squared(n))

		while slow!=fast and fast!=1:
			slow = self.squared(slow)
			fast = self.squared(self.squared(fast))

		return fast==1

	def squared(self, n):
		return sum([int(d)**2 for d in str(n)])    

