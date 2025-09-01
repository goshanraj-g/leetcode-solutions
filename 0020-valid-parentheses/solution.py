class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {"{":"}", "[":']', "(":")"}
        stack = []
        for p in s:
            if p in mappings:
                stack.append(p)
            else:
                if not stack or not mappings[stack[-1]] == p:
                    return False
                stack.pop()
        return not stack
