
class Solution:
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        parent = [-1] * n
        visited = [False] * n
        queue = deque([0])
        visited[0] = True
        
        while queue:
            curr = queue.popleft()
            for neighbor in adj[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = curr
                    queue.append(neighbor)
        
        total_time = 0
        
        visited_edges = [False] * n 
        
        for i in range(n):
            if hasApple[i]:
                curr = i
                
                while curr != 0 and not visited_edges[curr]:
                    visited_edges[curr] = True
                    total_time += 2 
                    curr = parent[curr] 
                    
        return total_time

            
            
            
            
        