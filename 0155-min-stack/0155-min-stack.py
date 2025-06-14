class MinStack(object):

    def __init__(self):
        self.buf=[] #initalise the stack as a list,dynamic one
        self.min=[]

        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.buf.append(val)
        if not self.min:
            self.min.append(val)
        else:
            self.min.append(min(self.min[-1],val))

        

    def pop(self):
        """
        :rtype: None
        """
        self.buf.pop()
        if self.min:
            self.min.pop()
    
        

    def top(self):
        """
        :rtype: int
        """
        return self.buf[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1] if self.min else 0        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()