class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        answer = float('inf')

        for i in range(n-2): #window of 2
            l, r = i+1, n - 1
            while l < r:
                threesum = nums[i] + nums[l] + nums[r]
                if abs(threesum - target) < abs(target-answer):
                    answer = threesum
                if threesum > target:
                    r -= 1
                elif threesum < target:
                    l += 1
                else:
                    return target
        return answer

                

        # to find if closest, subtract the numbers, and get the min
        
