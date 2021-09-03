#https://leetcode.com/problems/basic-calculator-ii/
# Medium
# First thought should be stack.
# Next thought should be how can I store the PREVIOUS sign.

class Solution(object):
    def calculate(self, s):
        s += '+'            # This is a really handy trick to avoid having to deal with a hanging number at the end of the expression.
        currSign = '+'
        nums = []
        currNum = 0

        for i in range(len(s)):
            if s[i].isnumeric():
                currNum = currNum * 10 + int(s[i])
            elif s[i] == ' ':
                pass
            else:
                if currSign == '+':
                    nums.append(currNum)
                elif currSign == '-':
                    nums.append(-currNum)
                elif currSign == '*':
                    nums.append(nums.pop() * currNum)
                else:
                    tmp = nums.pop()                    # Have to do this because if last num is -3 and currNum = 2, Python2 divides to -2 instead of -1
                    if tmp < 0:
                        nums.append( -(-tmp // currNum))
                    else:
                        nums.append( tmp // currNum)
                currNum, currSign = 0, s[i]
        return sum(nums)
        """
        :type s: str
        :rtype: int
        """
        