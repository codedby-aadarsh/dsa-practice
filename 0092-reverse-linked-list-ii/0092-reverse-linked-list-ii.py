# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        prev = None
        start = head
        # Step 1: Move to the node at position `left`
        for _ in range(left - 1):
            prev = start
            start = start.next

        curr = start
        tempPrev = None
        # Step 2: Reverse from `left` to `right`
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = tempPrev
            tempPrev = curr
            curr = temp

        # Step 3: Reconnect the reversed portion
        if prev:
            prev.next = tempPrev  # connect node before `left` to new head of reversed part
        else:
            head = tempPrev  # if reversing from head, update head

        start.next = curr  # connect tail of reversed portion to remainder

        return head
