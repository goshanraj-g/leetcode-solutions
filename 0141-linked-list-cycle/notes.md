# **Approach**
- Initialize a slow and fast pointer
- while the current fast pointer and fast.next pointer exist, initialize a loop

# **Solution**
<pre>
class Solution(object):
  def hasCycle(self, head) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        return True
    return False
</pre>

## **Time and Space Complexity**
**Time Complexity: O(n+m), where n and m are the lengths of the two lists**
**Space Complexity: O(1), there are no new allocations of memory (we are just relinking existing nodes), except for pointers which are constant time**

## **Key Ideas**
This is a simple **Singly Linked List** problem
