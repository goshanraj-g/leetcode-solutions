class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = {}
        for word in strs:
            sorted_word = str(sorted(word))
            
            if sorted_word not in anagrams:
                anagrams[sorted_word] = [word]
            else:
                anagrams[sorted_word].append(word)
        return list(anagrams.values())
