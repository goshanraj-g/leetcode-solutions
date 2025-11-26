class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        visited = set()
        components = 0

        def dfs(i):
            visited.add(i)
            for j in range(len(isConnected)):
                if j not in visited and isConnected[i][j] == 1:
                    dfs(j)

        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                components += 1
        return components
        
