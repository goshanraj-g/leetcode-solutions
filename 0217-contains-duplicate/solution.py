class Solution(object):
    def containsDuplicate(self, nums):
        duplicates = set(nums)
        if len(duplicates) == len(nums):
            return False
        return True

        """
        :type nums: List[int]
        :rtype: bool
        """
        
