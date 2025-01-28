class Solution(object):
    def twoSum(self, nums, target):

        stored_val = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in stored_val:
                return [stored_val[difference], i]

            stored_val[nums[i]] = i
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
