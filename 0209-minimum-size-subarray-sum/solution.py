class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        total = 0
        min_len = float('inf')

        for r in range(n):
            total += nums[r]
            while total >= target:
                min_len = min(min_len, r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if min_len == float('inf') else  min_len
