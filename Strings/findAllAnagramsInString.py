class Solution(object):
    def findAnagrams(self, s, p):
        rs = []
        anaCountFinal = defaultdict(int)
        anaCount = defaultdict(int)

        for c in p:
            anaCountFinal[c] += 1
            
        for i, c in enumerate(s):
            if sum(anaCount.values()) == len(p):
                if all(c in anaCount and anaCountFinal[c] == anaCount[c] for c in anaCountFinal):
                    rs.append(i- len(p))
                anaCount[s[i-len(p)]] -= 1
            anaCount[c] += 1
            
        if sum(anaCount.values()) == len(p):
            if all(c in anaCount and anaCountFinal[c] == anaCount[c] for c in anaCountFinal):
                rs.append(i-(len(p)-1))
            anaCount[s[i-len(p)]] -= 1
        return rs
                    
            
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
# First, we have to create a hash map with letters from p as keys and its frequencies as values. 
# Then, we start sliding the window [0..len(s)] over the s. 
# Every time a letter gets out of the window, we increase the corresponding counter in the hashmap, and when a letter gets in the window - we decrease. 
# As soon as all counters in the hashmap become zeros we encountered an anagram.
    def findAnagrams(self, s, p):
    	res = []
        letterMap, pL, sL = defaultdict(int), len(p), len(s)
        if pL > sL: return []

        # build hashMap
        for ch in p: 
        	letterMap[ch] += 1

        # initial full pass over the window
        for i in range(pL-1):
            if s[i] in letterMap: letterMap[s[i]] -= 1
            
        # slide the window with stride 1
        for i in range(-1, sL-pL+1): # From beginning to end-len(p) where p is the string we're checking against.
            if i > -1 and s[i] in letterMap: 	# If we're not at the start and the letter is in p, then add to P.
                letterMap[s[i]] += 1
            if i+pL < sL and s[i+pL] in letterMap: # If we're not at the bound of sL and the ending char of our window is in the p letterMap.
                letterMap[s[i+pL]] -= 1			# Then remove ending letter from letterMap.
                
            # check whether we encountered an anagram
            if all(v == 0 for v in letterMap.values()): # If all letters equal to 0, then we found an anagram. 
                res.append(i+1)
                
        return res
