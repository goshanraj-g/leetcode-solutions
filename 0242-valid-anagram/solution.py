class Solution(object):
    def isAnagram(self, s, t):
        smap = {}
        tmap = {}
        for char in s:
            smap[char] = smap.get(char, 0) + 1
        for char in t:
            tmap[char] = tmap.get(char, 0) + 1
        return smap == tmap
        
