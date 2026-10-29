class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        coursePreReq = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            coursePreReq[crs].append(pre)
        
        def valid(crs):
            if crs in visited:
                return False
            visited.add(crs)
            for pre in coursePreReq[crs]:
                if not valid(pre):
                    return False
            visited.remove(crs)
            coursePreReq[crs] = []
            return True
        
        for crs in coursePreReq:
            if not valid(crs):
                return False
        return True
