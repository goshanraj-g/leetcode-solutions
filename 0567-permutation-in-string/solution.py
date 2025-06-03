class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # build frequency map for s1 and for the first window of s2
        s1Count, s2Count = {}, {}
        for i in range(len(s1)):
            s1Count[s1[i]] = s1Count.get(s1[i], 0) + 1
            s2Count[s2[i]] = s2Count.get(s2[i], 0) + 1

        # count how many chars already match exactly between s1Count and s2Count
        matches = 0
        for char in s1Count:
            if s1Count[char] == s2Count.get(char, 0):
                matches += 1

        l = 0
        # slide the window over s2
        for r in range(len(s1), len(s2)):
            # if all distinct chars in s1 match in the current s2 window, return true
            if matches == len(s1Count):
                return True

            # add the new char at s2[r]
            char = s2[r]
            if char in s1Count:
                s2Count[char] = s2Count.get(char, 0) + 1
                # if new count equals s1Count[char], we gained a match
                if s2Count[char] == s1Count[char]:
                    matches += 1
                # if by incrementing we overshot s1Count[char], we lose a match
                elif s2Count[char] - 1 == s1Count[char]:
                    matches -= 1
            else:
                # if char is not in s1Count, still record it in s2Count
                s2Count[char] = s2Count.get(char, 0) + 1

            # remove the old leftmost char at s2[l]
            left_char = s2[l]
            if left_char in s1Count:
                # decrement its count
                s2Count[left_char] -= 1
                # if after decrementing it now equals s1Count[left_char], we gained a match
                if s2Count[left_char] == s1Count[left_char]:
                    matches += 1
                # if before decrementing it was exactly s1Count[left_char], we lose that match now
                elif s2Count[left_char] + 1 == s1Count[left_char]:
                    matches -= 1

                # if its count fell to zero, remove the key entirely
                if s2Count[left_char] == 0:
                    del s2Count[left_char]
            else:
                # if left_char wasnt in s1Count, just decrement or delete it
                s2Count[left_char] -= 1
                if s2Count[left_char] == 0:
                    del s2Count[left_char]

            l += 1

        # final check on the last window
        return matches == len(s1Count)

