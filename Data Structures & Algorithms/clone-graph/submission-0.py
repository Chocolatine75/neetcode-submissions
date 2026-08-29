"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        new ={} 
        new[node]=Node(node.val)
        q = deque()
        q.append(node)

        while q:
            current_Node = q.popleft()

            for n in current_Node.neighbors:
                if n not in new:
                    new[n] = Node(n.val)
                    q.append(n)
                new[current_Node].neighbors.append(new[n])
        return new[node]


            
        
    


