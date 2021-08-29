#https://leetcode.com/problems/text-justification/
class Solution(object):
    # 1. First, lets get the correct words into each line
    # 2. Lets split the remaining whitepsace based on (maxWidth - len(words))
    def fullJustify(self, words, maxWidth):
        rsp, curr, tempW = [], [], 0
        for w in words:
            if len(curr) + len(w) + tempW > maxWidth:
                size = max(1, len(curr) - 1)
                for i in range(0, maxWidth-tempW):
                    index = i%size
                    curr[index] += " "
                rsp.append( ''.join(curr) )
                curr = []
                tempW = 0
            curr += [w]
            tempW += len(w)

        rsp.append( " ".join(curr).ljust(maxWidth) )
        return rsp