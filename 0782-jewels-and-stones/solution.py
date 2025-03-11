class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        count = 0
        set_s = set(jewels)
        for char in range(len(stones)):
            if stones[char] in set_s:
                count += 1
        return count
