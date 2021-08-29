#https://leetcode.com/problems/decode-string/
class Solution(object):
    def decodeString(self, s):
        stack, currString, currNum = [], "", ""

        for char in s:
            if char == "]":
                currString *= int(stack.pop())
                currString = stack.pop() + currString
            elif char == "[":
                stack.append(currString)
                stack.append(currNum)
                currString = ""
                currNum = ""            
            elif char.isnumeric():
                currNum += char
            else:
                currString += char
        return currString