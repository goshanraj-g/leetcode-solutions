class Solution(object):
    def longestCommonPrefix(self, strs):
        #empty case, if it's empty return nothing
        if not strs:
            return ""

        #use first word as the one to compare everything else with
        prefix = strs[0]

        for string in strs[1:]:
            while string[:len(prefix)] != prefix:
                prefix = prefix [:-1]
                if not prefix:
                    return ""
        return prefix
            
                
            

