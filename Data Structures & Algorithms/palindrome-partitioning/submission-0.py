class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def ispali(string, l,r):
         
            while  l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1

            return True

        res,path = [],[]
        ls = len(s)
        def back(index):

            if index >= len(s):
                res.append(path[:])
                return

            for i in range(index,ls):

                if ispali(path,index,i):
                    path.append(s[index:i+1])
                    back(i+1)
                    path.pop()
        back(0)
        return res

                
