"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        old_new={}
        if not head:
            return None
        curr=head
        while(curr):
            old_new[curr]=Node(curr.val)
            curr=curr.next
        
        curr=head
        while(curr):
            old_new[curr].next=old_new.get(curr.next)
            old_new[curr].random=old_new.get(curr.random)
            curr=curr.next
        
        return old_new[head]