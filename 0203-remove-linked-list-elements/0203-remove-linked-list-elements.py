# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        dummyHead = ListNode(0) #creation of dummy node for the new head
        dummyHead.next = head#next node of the dummy node is the linked list we are provided 
        node = dummyHead#its not head, bc in the end we have to return just the value of new head

        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next

        return dummyHead.next

        