class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = []
        visit = set()
        for i in range(numCourses):
            adj.append([])
        for u,v in prerequisites:
            adj[u].append(v)
                
        def dfs(n):
            if n in visit:
                return False
            
            if adj[n] == []:
                return True
            
            visit.add(n)
            for pre in adj[n]:
                if not dfs(pre):
                    return False
            visit.remove(n)
            adj[n] =[]
            return True

        for i in range(numCourses):

            if not dfs(i):
                return False
        return True  

            

        



        