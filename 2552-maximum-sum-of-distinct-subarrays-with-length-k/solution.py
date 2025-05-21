class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if n < k:
            return 0

        window_sum = 0
        window_set = set()
        left = 0
        max_sum = 0

        for r in range(n):
            while nums[r] in window_set:
                window_set.remove(nums[left])
                window_sum -= nums[left]
                left += 1
            window_set.add(nums[r])
            window_sum += nums[r]
            
            if r - left + 1 == k:
                max_sum = max(window_sum, max_sum)
                window_set.remove(nums[left])
                window_sum -= nums[left]
                left += 1
        return max_sum
