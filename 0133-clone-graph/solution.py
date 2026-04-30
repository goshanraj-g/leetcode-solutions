"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        cloned = {}
        visited = set()

        def dfs(node):
            if node in visited:
                return None
            cloned[node.val] = Node(node.val, [])
            visited.add(node)
            for neighbor in node.neighbors:
                dfs(neighbor)
                cloned[node.val].neighbors.append(cloned[neighbor.val])
                visited.add(neighbor)
        dfs(node)
        return cloned[node.val]
