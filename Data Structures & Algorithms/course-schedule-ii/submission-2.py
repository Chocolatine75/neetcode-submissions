class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        premap = []
        for i in range(numCourses):
            premap.append([])
        
        for u,v in prerequisites:
            premap[u].append(v)
        output = []
        visit,cycle = set(),set()
        def dfs(n):

            if n in cycle:
                return False
            if n in visit:
                return True
            
            cycle.add(n)

            for curr in premap[n]:
                if dfs(curr) == False:
                    return False

            cycle.remove(n)
            visit.add(n)
            output.append(n)
            return True

        for i in range(numCourses):
            if dfs(i)==False:
                return []
        return output

        