class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest_substring = 0
        dup_set = set()
        for i in range(len(s)):
            while s[i] in dup_set:
                dup_set.remove(s[l])
                l += 1
            dup_set.add(s[i])
            longest_substring = max(longest_substring, i - l + 1)
        return longest_substring


