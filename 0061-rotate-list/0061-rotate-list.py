# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k==0:
            return head
        curr=head
        node=[]
        while(curr):
            node.append(curr)
            curr=curr.next
        k = k % len(node)  # Handle cases where k > len(arr)
        node=node[-k:] + node[:-k]
        node[k-1].next=node[k]
        node[len(node)-1].next=None
        head=node[0]
        return head

      

        