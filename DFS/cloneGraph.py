#https://leetcode.com/problems/clone-graph/
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return node
        
        nodestack = [node]
        nodemap = {node: Node(node.val)}
        
        while (nodestack):
            current_node = nodestack.pop()            
            for neighbor in current_node.neighbors:
                if neighbor not in nodemap:
                    nodestack.append(neighbor)
                    nodemap[neighbor] = Node(neighbor.val)
                nodemap[current_node].neighbors.append(nodemap[neighbor])
        return nodemap[node]
        """
        :type node: Node
        :rtype: Node
        """
        