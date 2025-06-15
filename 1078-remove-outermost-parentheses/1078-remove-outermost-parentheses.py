class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        c=''
        for i in s:
            if i=='(':
                if stack:
                    c+=i
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    c+=i
        return c