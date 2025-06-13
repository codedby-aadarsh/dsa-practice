class Solution(object):
    def isValid(self, s):
        stack=[]
        dic={')':'(','}':'{',']':'['}
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            elif ch in dic:
                if not stack or stack[-1]!=dic[ch]:
                    return  False
                stack.pop()
        return not stack
