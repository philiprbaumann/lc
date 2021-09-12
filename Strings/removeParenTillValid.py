# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# Got this one right off the bat.
# One thing to speed up the answer is to edit in place.
# Something to remember too...convert to list first!!
class Solution(object):
    def minRemoveToMakeValid(self, s):
        s = list(s)
        stackIndex = []
        
        for i, char in enumerate(s):
            if char == ')':
                if stackIndex:
                    stackIndex.pop()
                else:
                    s[i] = ''
            elif char == '(':
                stackIndex.append(i)
        
        while (stackIndex):
            s[stackIndex.pop()] = ''
            
        return "".join(s)
                
        """
        :type s: str
        :rtype: str
        """
        