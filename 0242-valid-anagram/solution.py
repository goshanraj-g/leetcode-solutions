class Solution(object):
    def isAnagram(self, s, t):
        list1 = []
        list2 = []
        for char in s:
            list1.append(char)
        for char in t:
            list2.append(char)
        list1.sort()
        list2.sort()
        if list1 == list2:
            return True
        else:
            return False
 
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
