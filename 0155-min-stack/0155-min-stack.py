class MinStack(object):

    def __init__(self):
        self.buf=[] #initalise the stack as a list,dynamic one

        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.buf.append(val)

        

    def pop(self):
        """
        :rtype: None
        """
        self.buf.pop()
    
        

    def top(self):
        """
        :rtype: int
        """
        return self.buf[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.buf)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()