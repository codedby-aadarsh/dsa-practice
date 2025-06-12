
class Solution(object):
    def swapNodes(self, head, k):
        #two pointer apparoch used here
        p1=p2=head
        for i in range(k-1):
            p2=p2.next
        res1=p2 #starting kth value we get
        while(p2.next):
            p1=p1.next
            p2=p2.next
        #p1 reaches the kth value from the last and we perform the swap
        res1.val,p1.val=p1.val,res1.val
        return head


