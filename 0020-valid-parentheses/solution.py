class Solution(object):
    def isValid(self, s):
        mappings = {")":"(", "}":"{", "]":"["}
        stack = []
        for char in s:
            if char in mappings:
                if stack and stack[-1] == mappings[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if len(stack) == 0 else False
        
