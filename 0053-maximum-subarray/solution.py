class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSubarray = 0
        maxVal = float("-inf")
        for i in range(len(nums)):
            if maxSubarray < 0:
                maxSubarray = 0
            maxSubarray += nums[i]
            maxVal = max(maxSubarray, maxVal)
        return maxVal
