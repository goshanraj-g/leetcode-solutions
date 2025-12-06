class Solution:
    def calculate_sum(self, nums: List[int], D: int) -> int:
        total_sum = 0
        for num in nums:
            total_sum += math.ceil(num / D)
        return int(total_sum)
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        l = 1
        r = max(nums)

        res = r

        while (l <= r):
            mid = (l + r) // 2
            val = self.calculate_sum(nums, mid)

            if val <= threshold:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

        # for each element we have to divide the number by chosen, and 
        # use binary search starting at 
