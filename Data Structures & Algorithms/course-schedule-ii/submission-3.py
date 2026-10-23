class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        map = {i:[] for i in range(numCourses)}
        res = [] 

        for crs, pre in prerequisites: 
            map[crs].append(pre)
        
        visited, path = set(), set() 
        def dfs(crs):
            if crs in visited:
                return True
            if crs in path:
                return False
            path.add(crs)
            for pre in map[crs]:
                if not dfs(pre):
                    return False
            path.remove(crs)
            visited.add(crs)
            map[crs] = []
            res.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
            