class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()
        distance = 0

        def replace(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or ((r,c) in visited) or grid[r][c] == -1):
                return
            visited.add((r,c))
            q.append([r,c])
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append([r,c])
 
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                replace(r+1,c)
                replace(r-1,c)
                replace(r,c+1)
                replace(r,c-1)
            distance += 1