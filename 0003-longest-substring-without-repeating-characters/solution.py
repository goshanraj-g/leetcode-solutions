class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checkSet = set()

        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in checkSet:
                checkSet.remove(s[l])
                l += 1
            
            checkSet.add(s[r])
            res = max(res, len(checkSet))

        return res


            


        # sliding window approach
        # create a set
        # if adding new element ruins the unique fact
            # keep removing from left side until no more duplicates
        # if new element not ruin unique
            # we add rightmost element of the window to the result, and calculate
        
