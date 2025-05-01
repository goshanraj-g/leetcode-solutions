# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):

        dummy = ListNode()
        tail = dummy
        
        cur1 = list1
        cur2 = list2

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                tail.next = cur1
                cur1 = cur1.next
            else:
                tail.next = cur2
                cur2 = cur2.next
            tail = tail.next
        if cur1:
            tail.next = cur1
        else:
            tail.next = cur2
        return dummy.next

        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
