# https://leetcode.com/problems/encode-and-decode-strings/  

class Codec:

    def encode(self, strs):
        return ''.join([ "%d:" % len(s) + s for s in strs])
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        

    def decode(self, s):
        strs = []
        i = 0
        while i < len(s):
            j = s.find(':', i)
            i = j + 1 + int(s[i:j])
            strs.append(s[j+1:i])
            
        return strs
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))