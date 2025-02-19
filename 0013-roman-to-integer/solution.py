class Solution(object):
    def romanToInt(self, s):
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0

        for i in range((len(s)-1), -1, -1):
            if i+1 == len(s):
                total += mapping[s[i]]
            elif mapping[s[i]] < mapping[s[i+1]]:
                total -= mapping[s[i]]
            else:
                total += mapping[s[i]]
        return total




        """
        :type s: str
        :rtype: int
        """
        
