class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head=None
        self.size=0
        

    def get(self, index):
        if index<0 or index>=self.size:
            return -1
        curr=self.head
        for i in range(index):
            curr=curr.next
        return curr.val


        

    def addAtHead(self, val):
       self.addAtIndex(0,val)
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size,val)
        

    def addAtIndex(self, index, val):
        if index > self.size:
            return

        new_node = Node(val)

        if index <= 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev = self.head
            for i in range(index - 1):
                prev = prev.next
            new_node.next = prev.next
            prev.next = new_node

        self.size += 1
  

        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        if index==0:
            self.head=self.head.next
        else:
            curr=self.head
            for i in range(index-1):
                curr=curr.next
            curr.next=curr.next.next
        self.size-=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)