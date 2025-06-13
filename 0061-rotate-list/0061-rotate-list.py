class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k==0:
            return head
        n=1
        curr=head
        while(curr.next):
            n+=1
            curr=curr.next
        curr.next=head
        k=k%n
        temp=head
        for i in range(n-k-1):
            temp=temp.next
        head=temp.next
        temp.next=None
        return head

        
      

        