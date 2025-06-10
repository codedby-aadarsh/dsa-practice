# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        li=[]
        node=head
        while(node):
            li.append(node.val)
            node=node.next
        li=li[::-1]
        sum=0
        for i in range(len(li)):
            sum+=li[i]*2**i
        return sum
