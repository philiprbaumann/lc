#https://leetcode.com/problems/reverse-bits/
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        answer = 0
        for x in range(32):
            answer = (answer << 1) + (n & 1)
            n >>= 1
            
        return answer