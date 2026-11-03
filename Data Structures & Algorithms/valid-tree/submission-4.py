class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        visited = []
        adjList = { i:[] for i in range(n)}

        for s, e in edges:
            adjList[s].append(e)
            adjList[e].append(s)
        
        def dfs(node, prev):
            if node in visited:
                return False
            visited.append(node)
            for child in adjList[node]:
                if child == prev:
                    continue
                if not dfs(child, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n

                
        