# Here's an answer with bad runtime and bad memory usage: O(N^2) runtime complexity and O(N) space.
# After doing that, I definitely remember there being a way to increment either the first pointer or 
# the last pointer dependent on what's going on.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        letters = {}
        max_length = 1
        for start in range(len(s)):
            for i in range(start, len(s)):
                if s[i] in letters:
                    break
                letters[s[i]] = True
                max_length = max(max_length, i - start+1)
            letters = {}
        return max_length

# We're getting closer, but it's not how refined as I want it to be. I think the interior
# while loop is a little sloppy and can be done better. This is just a base use of a queue. 
# There's a better approach here that removes the queue by storing the index of the character
# which is better use of the dictionary and means we don't need an extra queue. 
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        letter_count = {}
        queue = []
        max_length = 1

        for i in range(len(s)):
            queue.append(s[i])
            while(True):
                if s[i] in letter_count and letter_count[s[i]] != 0: 
                    letter_count[queue.pop(0)] = 0
                else:
                    letter_count[s[i]] = 1
                    break
            max_length = max(max_length, len(queue))
        return max_length


# Alright here is the most efficient sliding window approach as far as I know.
# The trick here is to remember the dictionary to letter index approach
# which can definitely be pretty handy. 
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, max_length, letter_location = {}
        for i, char in enumerate(s):
            if char in letter_location and start <= letter_location[char]:  # If the character has already been seen, let's go to the last index of the character
                start = letter_location[char] + 1                           # and then move one forwards so that we no longer include that character.
            else:
                max_length = max(max_length, i - start + 1)                 # If we haven't seen this character before, then let's measure the max length because
                                                                            # if we've seen it before, then the max CANNOT increase given window just slide right once on both lower and upper bounds. 
            letter_location[char] = i                                       # No matter what, we have to set the index of the current character.
        return max_length

# Past the index dictionary, it just comes down to some basic math and 
# the understanding that the:
#		MAX_LENGTH WILL NOT INCREASE IF WE HAVE SEEN THE LETTER BEFORE