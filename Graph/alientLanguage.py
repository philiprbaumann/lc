# https://leetcode.com/problems/alien-dictionary
# Topological sort again
class Solution(object):
    
    # This is the general topological sort approach. 
    # Visited array to track state with 1, 0, or 1
    # Graph is the adjacency matrix with sets 
    # ANS is the stack we're slowly building and then reversing on answer. 
    def dfs(self, node, visited, graph, ans):
        visitedNumber = ord(node)-ord('a')              # ord == unicode code for character
        if visited[visitedNumber] == -1: return False
        if visited[visitedNumber] == 1: return True
        
        visited[visitedNumber] = -1
        
        if node in graph:
            for x in graph[node]:
                if not self.dfs(x, visited, graph, ans):
                    return False
                
        visited[visitedNumber] = 1
        ans.append(node)
        return True
    
    def alienOrder(self, words):
        visited = [0 for _ in range(26)]
        ans = []
        chars = set("".join(words))
        graph = defaultdict(set)

        # This is the hard part of the question.
        # Zip words together to iterate over 0:n / 1:n-1
        for pair in zip(words, words[1:]):
            # This is an invalid edge case -> ['abc', 'ab']
            # Kind of a bullshit case, but one that I'd need to consider in a real test.  
            if len(pair[0]) > len(pair[1]) and pair[0].startswith(pair[1]): return ""
            for c1, c2 in zip(*pair):
                if c1 != c2:
                    graph[c1].add(c2)
                    break
        
        for c in chars:
            visitedNumber = ord(c)-ord('a')
            if visited[visitedNumber] != 1:
                if not self.dfs(c, visited, graph, ans):
                    return ""
                
        return ''.join(ans[::-1])

        """
        :type words: List[str]
        :rtype: str
        """
        