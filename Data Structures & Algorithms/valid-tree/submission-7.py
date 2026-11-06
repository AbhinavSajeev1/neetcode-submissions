class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: 
            return True
        valid = [] 
        adjList = {i:[] for i in range(n)}

        for node, child in edges:
            adjList[node].append(child)
            adjList[child].append(node)

        [[0,1],[1,2],[2,3],[1,3],[1,4]]

        

        VALID =[0]        
        
        
        def dfs(curr, prev):
            if curr in valid:
                return False
            valid.append(curr)
            for child in adjList[curr]:
                if prev == child:
                    continue
                if not dfs(child, curr):
                    return False
            return True
        return dfs(0, -1) and len(valid) == n

                