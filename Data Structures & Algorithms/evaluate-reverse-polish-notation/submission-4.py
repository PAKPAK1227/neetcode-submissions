class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i != '+' and i != '-' and i != '*' and i != '/':
                stack.append(i)
            else:
                second_val = int(stack.pop())
                first_val = int(stack.pop())
                if i == '+':
                    stack.append(str(first_val + second_val))
                elif i == '-':
                    stack.append(str(first_val - second_val))
                elif i == '*':
                    stack.append(str(first_val * second_val))
                elif i == '/':
                    stack.append(str(int(first_val / second_val)))
        return int(stack.pop())
