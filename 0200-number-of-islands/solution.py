class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # iterate through each cell in the grid
        # if you found an island, increment by 1
        # check the neighbors (up, down, left, right)
        # keep track of marked, and unmarked nodes in a set w/ coordinates
        # when no longer 1's end and continue to next node which is unmarked
        if not grid:
            return 0
    
        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows)) and ((c in range(cols)) and (grid[r][c] == '1') and ((r, c) not in visited)):
                        q.append((r, c))
                        visited.add((r , c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    count += 1

        return count

            




