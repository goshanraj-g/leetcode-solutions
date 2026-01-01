class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if len(ransomNote) > len(magazine):
            return False
        mmap = {}
        for char in magazine:
            mmap[char] = mmap.get(char, 0) + 1

        for char in ransomNote:
            if mmap.get(char, 0) > 0:
                mmap[char] = mmap.get(char, 0) - 1
            else:
                return False
        return True

        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
