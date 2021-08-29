#https://leetcode.com/problems/fizz-buzz/
class Solution(object):
    def fizzBuzz(self, n):
        i = 1
        answer = []
        while (i<n+1):
            if (i%3 == 0 and i%5 == 0):
                answer.append("FizzBuzz")
            elif (i%3==0):
                answer.append("Fizz")
            elif (i%5==0):
                answer.append("Buzz")
            else:
                answer.append(str(i))
            i = i+1
        return answer
        """
        :type n: int
        :rtype: List[str]
        """