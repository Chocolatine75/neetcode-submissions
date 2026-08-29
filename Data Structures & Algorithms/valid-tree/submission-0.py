class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = []
        for i in range(n):
            adj.append([])
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        q =deque([(0,-1)])
        visit.add(0)
        while q:
            node,parent = q.popleft()
            for no in adj[node]:
                if no == parent:
                    continue
                if no in visit:
                    return False
                visit.add(no)
                q.append((no,node))
        return len(visit) ==n
                

        
        