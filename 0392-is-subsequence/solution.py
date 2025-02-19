class Solution(object):
    def isSubsequence(self, s, t):

        res = ""
        default = 0
        if len(s) == 0:
            return True
        for i in range(len(t)):
            if t[i] == s[default]:
                res += t[i]
                default += 1
            if default == len(s):
                return res == s
        return res == s
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
