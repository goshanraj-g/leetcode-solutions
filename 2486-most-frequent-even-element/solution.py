class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count = {}
        for n in nums:
            if n % 2 == 0:
                count[n] = count.get(n, 0) + 1
        if not count:
            return -1

        return min(count.items(), key=lambda x: (-x[1], x[0]))[0]

        

        
