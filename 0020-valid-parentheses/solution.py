class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {")":"(", "}":"{","]":"["}
        for char in s:
            if char in mapping:
                if len(stack) > 0:
                    val = stack.pop()
                else:
                    return False
                if mapping[char] != val:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
