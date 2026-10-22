class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path = set() 
        preReqMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites: 
            preReqMap[crs].append(pre)

        def dfs(crs):
            if crs in path:
                return False
            if preReqMap[crs] == []:
                return True
            path.add(crs)
            for pre in preReqMap[crs]:
                if not dfs(pre):
                    return False
            path.remove(crs)
            preReqMap[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True 