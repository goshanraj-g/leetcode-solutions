class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums) -1
        answer = []

        for i in range(n):
            # no way for the sums to be equal to 0
            if nums[i] > 0:
                break
            # duplicates
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1, n
            while l < r:
                threesum = nums[i] + nums[l] + nums[r]
                if threesum == 0:
                    answer.append([nums[i], nums[l], nums[r]])
                    l, r = l + 1, r - 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -=1
                elif threesum < 0:
                    l += 1
                else:
                    r -=1
        return answer



        
