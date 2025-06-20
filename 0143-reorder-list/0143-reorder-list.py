# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=fast=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        curr=slow.next
        prev=None
        while(curr):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        slow.next=None
        
        head1, head2 = head, prev
        while head1 and head2:
            old_h1_next = head1.next
            old_h2_next = head2.next
            
            head1.next = head2
            head2.next = old_h1_next

            head1 = old_h1_next
            head2 = old_h2_next