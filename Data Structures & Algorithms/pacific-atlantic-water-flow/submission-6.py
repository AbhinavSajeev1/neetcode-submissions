class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []

        def dfs(r, c, visited, prevHeight):
            if (r<0 or c<0 or r >= ROWS or c >= COLS or ((r,c) in visited) or heights[r][c] < prevHeight):
                return
            visited.add((r,c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
        
        for i in range(ROWS):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, COLS-1, atl, heights[i][COLS-1])
        

        for r in range(ROWS):
            for j in range(COLS):
                if (r,j) in pac and (r,j) in atl:
                    res.append([r,j])
        return res