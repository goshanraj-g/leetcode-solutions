class Solution(object):
    def twoSum(self, nums, target):
        vals = {}
        for num in range(len(nums)):
            difference = target - nums[num]
            if difference in vals.keys():
                return [vals[difference], num]
            vals[nums[num]] = num
