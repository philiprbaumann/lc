# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# The trick with this one is realizing recursion can come in handy. 
# Originally thought iteratively, but creating a trie in this scenario isn't worth the headache.
class Solution(object):
        
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        letterMap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        ans = []
        def helper(ans, word, digits, i):
            if i == len(digits):
                ans.append(word)
                return
            
            for key in letterMap[digits[i]]:
                helper(ans, word+key, digits, i+1)
        
        helper(ans, "", digits, 0)
                    
        return ans
        
        """
        :type digits: str
        :rtype: List[str]
        """
        