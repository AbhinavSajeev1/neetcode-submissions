class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque() 
        visit = set() 

        
        def dfs(r,c):
            if (r<0 or c<0 or r==ROWS or c==COLS or (r,c) in visit or grid[r][c] == -1):
                return 
            visit.add((r,c))
            q.append([r,c])
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    visit.add((i,j))
                    q.append([i,j])
                    
        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)
            distance +=1 

