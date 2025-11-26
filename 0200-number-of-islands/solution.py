from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        NRows = len(grid)
        NCols = len(grid[0])
        queue = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        num_of_islands = 0

        for i in range(NRows):
            for j in range(NCols):

                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    queue.append((i, j))
                    num_of_islands += 1

                    while queue:
                        r, c = queue.popleft()
                        for direction in directions:
                            nr, nc = r + direction[0], c + direction[1]
                            if 0 <= nr < NRows and 0 <= nc < NCols and grid[nr][nc] == '1':
                                queue.append((nr, nc))
                                grid[nr][nc] = '0'
        
        return num_of_islands
