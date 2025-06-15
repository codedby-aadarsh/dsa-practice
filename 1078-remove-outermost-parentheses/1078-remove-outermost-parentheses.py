class Solution(object):
    def removeOuterParentheses(self, s):
        stack=0
        c=''
        for i in s:
            if i=='(':
                if stack:
                    c+='('
                stack+=1
            else:
                stack-=1
                if stack:
                    c+=')'
                
        return c