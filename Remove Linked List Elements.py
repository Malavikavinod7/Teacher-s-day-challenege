# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        # Create a dummy node that points to the head of the list
        dummy = ListNode(0)
        dummy.next = head

        current = dummy # Pointer to traverse the list
        
        # Traverse the list
        while current.next:
            if current.next.val == val:
                # If the next node's value matches val, skip it (remove it)
                current.next = current.next.next
            else:
                # Otherwise, move to the next node
                current = current.next
        
        # The new head is dummy.next
        return dummy.next
