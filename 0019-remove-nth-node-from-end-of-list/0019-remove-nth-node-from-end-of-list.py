# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        p1=p2=head
        for i in range(n):
            p2=p2.next
        if p2==None:
            return head.next
        else:
            while(p2.next):
                p1=p1.next
                p2=p2.next
            p1.next=p1.next.next
        return head
        
        