class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        longest = 0
        for n in nums:
            if (n-1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    numSet.remove(n + length)
                    length += 1
                longest = max(length, longest)
        return longest
        
