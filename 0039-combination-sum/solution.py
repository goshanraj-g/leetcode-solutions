class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        def dfs(i, total, path):
            if total == target:
                res.append(path[:])
                return
            if i == len(candidates) or total > target:
                return
            
            path.append(candidates[i])
            dfs(i, total + candidates[i], path)
            path.pop()

            dfs(i + 1, total, path)
        dfs(0, 0, [])
        return res


    # could be similar to subsets, but only add if sum if equal to target, and make it a set to avoid duplicates




