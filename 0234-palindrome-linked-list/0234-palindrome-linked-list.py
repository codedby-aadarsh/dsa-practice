# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        li=[]
        node=head
        while(node):
            li.append(node.val)
            node=node.next
        return li==li[::-1]