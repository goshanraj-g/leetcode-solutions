class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        r = 1
        res = s[0]
        curMax = 0

        while r < len(s):
            if s[r] not in res:
                res += s[r]
                r += 1
            else:
                curMax = max(curMax, len(res))
                dup_index = res.index(s[r])
                res = res[dup_index + 1:] + s[r]
                r += 1

        return max(curMax, len(res))

