class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for ch in tokens:
            if ch not in '+-*/':
                stack.append(int(ch))
            else:
                b = stack.pop()
                a = stack.pop()
                if ch == '+':
                    stack.append(a + b)
                elif ch == '-':
                    stack.append(a - b)
                elif ch == '*':
                    stack.append(a * b)
                elif ch == '/':
                    stack.append(int(float(a) / b))  # Ensures truncation toward zero
        return stack[0]
