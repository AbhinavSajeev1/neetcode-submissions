class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map = {i:[] for i in range(numCourses)}
        visited = set() 
        
        for crs, pre in prerequisites: 
            map[crs].append(pre)

        def valid(crs):
            if crs in visited:
                return False
            if map[crs] == []:
                return True
            visited.add(crs)
            for pre in map[crs]:
                if not valid(pre):
                    return False
            visited.remove(crs)
            map[crs] = [] 
            return True
                
        
        for i in range(numCourses):
            if not valid(i):
                return False
        return True

            