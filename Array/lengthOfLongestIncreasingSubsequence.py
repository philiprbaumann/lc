#https://leetcode.com/problems/longest-increasing-subsequence
class Solution(object):
    # O(N log N)
    def lengthOfLIS(self, nums):
        sub = []
        for num in nums:
            i = bisect_left(sub, num)

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)
            
            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num
        
        return len(sub)

    # O(N^2)
    def lengthOfLIS(self, nums):
        visited = []
        for num in nums:
            currLongest = max([v[1] for v in visited if v[0] < num] or [0]) + 1
            visited.append( (num, currLongest) )
        
        return max(visited, key=lambda x: x[1])[1]
        """
        :type nums: List[int]
        :rtype: int
        """
        