class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = []
        for i in range(n):
            adj.append([])
        visit = [False] *n
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def bfs(node):

            q = deque([node])
            visit[node]= True
            while q:
                cur = q.popleft()

                for no in adj[cur]:
                    if not visit[no]:
                        visit[no]=True
                        q.append(no)
        
        res = 0
        for node in range(n):
            if not visit[node]:
                bfs(node)
                res +=1
        return res




        