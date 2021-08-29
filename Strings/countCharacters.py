#https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
class Solution(object):
    def countCharacters(self, words, chars):
        char_count = collections.Counter(chars)
        sum = 0
        for word in words:
            word_count = collections.Counter(word)
            for count in word_count:
                if word_count[count] > char_count[count]:
                    break
            else:
                sum += len(word)
        return sum
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """