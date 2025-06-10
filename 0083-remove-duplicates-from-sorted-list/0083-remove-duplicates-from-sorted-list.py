# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node=head
        while(node and node.next):
            if node.val==node.next.val:
                node.next=node.next.next 
                continue
            node=node.next
        return head