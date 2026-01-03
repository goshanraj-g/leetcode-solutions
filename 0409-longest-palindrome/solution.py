class Solution(object):
    def longestPalindrome(self, s):
        daMap = {}
        for char in s:
            daMap[char] = daMap.get(char, 0) + 1
        length, isOdd = 0, False
        for values in daMap.values():
            if values % 2 == 0:
                length += values
            elif values == 1:
                if not isOdd:
                    length += 1
                    isOdd = True
            else:
                if not isOdd:
                    length += values
                    isOdd = True
                else:
                    length += values - 1
        return length
        

            
