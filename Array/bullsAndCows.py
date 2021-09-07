# https://leetcode.com/problems/bulls-and-cows/
import collections

class Solution(object):
    def getHint(self, secret, guess):
        secretCount, bulls, cows = collections.Counter(secret), 0, 0
        secret, guess = list(secret), list(guess)
        for i in range(0, len(secret)):
            if secret[i] == guess[i] and secretCount[ guess[i] ] != 0:
                bulls += 1
                secretCount[ secret[i] ] -= 1
                guess[i] = '#'
        for i in range(0, len(secret)):
            if guess[i] in secretCount and secretCount[ guess[i] ] != 0:
                cows += 1
                secretCount[ guess[i] ] -= 1
                
        return str(bulls)  + "A" + str(cows) + "B"       