class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_i  = set(nums)
        if len(set_i) == len(nums):
            return False
        return True
        
