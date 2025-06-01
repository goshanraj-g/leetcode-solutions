class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # first, sort the array
        # we can start with the first element, and find two other numbers 
        # if not found, move onto next number
        # ensure that the number is not a duplicate of the previous numbers
        # use a set to make sure no duplicates 

        nums.sort()
        first_dup = set()
        res = []

        for n in range(len(nums)):
            if nums[n] in first_dup:
                continue
            first_dup.add(nums[n])

            l, r = n + 1, len(nums) - 1

            while l < r:
                threesum = nums[l] + nums[r] + nums[n]

                if threesum == 0:
                    res.append([nums[n], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif threesum > 0:
                    r -= 1
                else:
                    l += 1 
        return res


                


        
