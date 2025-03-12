class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d1 = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
        d2 = {}
        for char in text:
            if char in d2.keys():
                d2[char] += 1
            else:
                d2[char] = 1

        minimumValue = 999999
        for char in d1:
            if char not in d2:
                return 0
            minimumValue = min(minimumValue, d2[char] // d1[char])
        return minimumValue

