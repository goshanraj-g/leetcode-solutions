class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSubstring = 0
        l = 0
        dupSet = set()
        for r in range(len(s)):
            while s[r] in dupSet:
                dupSet.remove(s[l])
                l += 1
            dupSet.add(s[r])
            current_window_size = r - l + 1
            maxSubstring = max(maxSubstring, current_window_size)
        return maxSubstring     


        char_set = set()
        l = 0
        
\

