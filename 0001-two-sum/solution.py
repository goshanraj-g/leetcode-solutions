class Solution(object):
    def twoSum(self, nums, target):

        # the approach for this question:
        # complement
        stored_val = {}

        for num in range(len(nums)):
            difference = target - nums[num]
            if difference in stored_val:
                return [stored_val[difference], num]
            stored_val[nums[num]] = num

