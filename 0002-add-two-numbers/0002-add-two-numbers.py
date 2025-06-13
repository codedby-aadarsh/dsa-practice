# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not l1 : return l2
        elif not l2:return l1
        elif not l1 and not l2: return None
        else:
            dummy=ListNode(0)
            curr=dummy
            p1=l1
            p2=l2
            carry=digit=0
            while p1 or p2 or carry:
                val1= p1.val if p1 else 0
                val2= p2.val if p2 else 0
                total=val1+val2+carry
                carry=total//10
                curr.next=ListNode(total%10)
                curr=curr.next
                p1=p1.next if p1 else None
                p2=p2.next if p2 else None
            return dummy.next
        
        
            
        