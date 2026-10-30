class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n 
        amount = 0 
        adjList = [[] for i in range(n)]
        
        for a, b in edges: 
            adjList[a].append(b)
            adjList[b].append(a)

        def dfs(node):
            for neighbor in adjList[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)
        
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                amount += 1
        return amount


