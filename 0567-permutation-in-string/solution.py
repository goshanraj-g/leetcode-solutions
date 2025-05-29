class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        window_size = len(s1)

        def char_to_index(c):
            return ord(c) - ord('a')

        s1_count = [0] * 26
        window = [0] * 26

        for c in s1:
            s1_count[char_to_index(c)] += 1

        for i in range(window_size):
            window[char_to_index(s2[i])] += 1

        if s1_count == window:
            return True

        for i in range(window_size, len(s2)):
            window[char_to_index(s2[i])] += 1
            window[char_to_index(s2[i - window_size])] -= 1

            if s1_count == window:
                return True

        return False

