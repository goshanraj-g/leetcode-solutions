class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stored_val = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in stored_val:
                return [stored_val[difference], i]
            stored_val[nums[i]] = i


