class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        visitedSet = set()
        rows = len(grid)
        cols = len(grid[0])

        directions = [(1,0), (-1,0), (0,-1),(0,1)]

        maxArea = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visitedSet:
                    q = deque()
                    q.append((r, c))
                    curArea = 1
                    while q:
                        cur_r, cur_c = q.popleft()
                        visitedSet.add((cur_r, cur_c))
                        for dir_r, dir_c in directions:
                            nr, nc = cur_r + dir_r, cur_c + dir_c
                            if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in visitedSet):
                                visitedSet.add((nr, nc))
                                q.append((nr, nc))
                                curArea += 1
                        maxArea = max(curArea, maxArea)
        return maxArea

