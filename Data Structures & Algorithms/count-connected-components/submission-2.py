class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n 
        count = 0
        adjList = [[] for _ in range(n)]

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        def dfs(node):
            for neighbor in adjList[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)            
                    
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                count += 1
        return count 
