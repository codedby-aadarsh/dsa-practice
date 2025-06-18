# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(-1) #made a dummy linked list for return
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val: #here we compare the list val with the second one and make the pointer to reference that one 
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Append remaining nodes
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy.next
