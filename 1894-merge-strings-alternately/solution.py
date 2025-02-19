class Solution(object):
    def mergeAlternately(self, word1, word2):
        shorter = min(len(word1), len(word2))
        res = ""
        for i in range(shorter):
            res += word1[i]
            res += word2[i]
        if not word2 in res:
            res += word2[shorter::]
        if not word1 in res:
            res += word1[shorter::]
        return res
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
