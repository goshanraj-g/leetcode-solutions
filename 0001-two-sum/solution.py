class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
