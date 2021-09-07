# https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie(object):

    def __init__(self):
        self.trie = {}
        """
        Initialize your data structure here.
        """
        

    def insert(self, word):
        if len(word) == 0:
            return
        t = self.trie
        for char in word:
            if char not in t:
                t[char] = {}
            t = t[char]
        t['#'] = '#'
        
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        

    def search(self, word):
        t = self.trie
        for char in word:
            if char in t:
                t = t[char]
            else:
                return False
        if "#" in t:
            return True
        return False
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        

    def startsWith(self, prefix):
        t = self.trie
        for char in prefix:
            if char in t:
                t = t[char]
            else:
                return False
        return True
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)