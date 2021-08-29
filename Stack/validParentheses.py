#https://leetcode.com/problems/valid-parentheses/
class Solution(object):
    def isValid(self, s):
        stack = []
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == ')' and stack and char == stack[-1]:
                stack.pop()
            elif char == '[':
                stack.append(']')
            elif char == ']' and stack and char == stack[-1]:
                stack.pop()
            elif char == '{':
                stack.append('}')
            elif char == '}' and stack and char == stack[-1]:
                stack.pop()
            else:
                return False
                
        return not stack
        """
        :type s: str
        :rtype: bool
        """
        