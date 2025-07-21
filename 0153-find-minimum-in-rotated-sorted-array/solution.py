class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[l] > nums[mid]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                return nums[l]
        return nums[r] if nums[l] < nums[r] else nums[l]
