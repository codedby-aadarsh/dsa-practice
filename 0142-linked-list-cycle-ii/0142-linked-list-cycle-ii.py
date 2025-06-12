# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None

        slow=fast=head
        
        while(fast and fast.next):
            fast=fast.next.next
            slow=slow.next
            if(fast==slow):
                break
        if not slow==fast : 
            return None
        else:
            slow=head
            while(slow!=fast):
                slow=slow.next
                fast=fast.next
            return slow