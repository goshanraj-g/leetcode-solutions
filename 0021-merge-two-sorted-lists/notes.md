# **Approach**
- Initialize a dummy ListNode to simplify tail/head management
- Initialize a pointer to dummy to track the end of the list
- Set a pointer for each list to traverse the outputs
- While both lists are non-empty, compare the values, add the smaller value to the tail and advance the list pointer and the tail pointer
- Once a list is empty, attach the remaining nodes to the tail
- Return the head (dummy.next)

# **Solution**
<pre>
class Solution(object):
  mergeTwoLists(self, list1, list2):
    dummy = ListNode()
    tail = dummy
    cur1, cur2 = list1, list2
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
</pre>

## **Time and Space Complexity**
**Time Complexity: O(n+m)**
**Space Complexity: O(n+m), where n and m are the lengths of the two lists**

## **Key Ideas**
This is a simple **Linked List** problem
