class Solution(object):
    def checkValidString(self, s):
        lstack = []
        pstack = []

        for i in range(len(s)):
            if s[i] == "(":
                lstack.append(i)
            elif s[i] == "*":
                pstack.append(i)
            else:
                if lstack:
                    lstack.pop()
                elif pstack:
                    pstack.pop()
                else:
                    return False
        
        while lstack and pstack:
            if lstack[-1] < pstack[-1]:
                lstack.pop()
                pstack.pop()
            else:
                return False

        return len(lstack) == 0
        """
        :type s: str
        :rtype: bool
        """
        
