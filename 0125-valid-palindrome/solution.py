class Solution(object):
    def isPalindrome(self, s):
        res = []
        for char in s:
            if char.isalnum():
                res.append(char.lower())
        return res == res[::-1]
