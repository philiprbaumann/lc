#https://leetcode.com/problems/find-center-of-star-graph/
class Solution(object):
    def findCenter(self, edges):
        return ''.join(map(str, set(edges[0]) & set(edges[1])))