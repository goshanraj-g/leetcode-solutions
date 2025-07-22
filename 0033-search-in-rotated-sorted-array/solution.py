class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            if nums[l] <= nums[m]: # IF IN LEFT SORTED
                if nums[m] < target or nums[l] > target: # CHECK IF TARGET SHOULD BE IN RS
                    l = m + 1
                else:
                    r = m - 1
            else: # IF IN RIGHT SORTED
                if nums[r] < target or nums[m] > target: # CHECK IF TARGET SHOULD BE IN LS
                    r = m - 1
                else:
                    l = m + 1
        return -1
        
