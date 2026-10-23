class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        visit = set()
        path = set()

        res = [] 

        def dfs(crs):
            if crs in visit:
                return True
            if crs in path: 
                return False
            path.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            path.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res 

        
        
        