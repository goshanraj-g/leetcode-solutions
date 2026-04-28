class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visitedSet = set()
        numIslands = 0

        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        # bfs implementation
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visitedSet:
                    numIslands += 1
                    q = deque()
                    q.append((r, c))
                    visitedSet.add((r,c))
                    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    while q:
                        row, col = q.popleft()
                        # check every direction here
                        for rr, cc in directions:
                            nr, nc = row + rr, col + cc
                            if ((0 <= nr < rows and 0 <= nc < cols) and (grid[nr][nc] == '1') and ((nr,nc) not in visitedSet)):
                                q.append((nr, nc))
                                visitedSet.add((nr, nc))
        return numIslands
