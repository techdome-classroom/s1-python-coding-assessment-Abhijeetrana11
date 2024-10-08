class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        island_count = 0
        
        def dfs(row, col):
            stack = [(row, col)]
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            while stack:
                r, c = stack.pop()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == 'L':
                        visited[nr][nc] = True
                        stack.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L' and not visited[r][c]:
                    island_count += 1
                    visited[r][c] = True
                    dfs(r, c)
        
        return island_count
    
        
        
