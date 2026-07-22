class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Remember integer division for negative number truncates torwards -infinity
        # integer division for positive numbers truncates torward zero
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
                else:
                    stack.append(str(int(first_val / second_val)))
        return int(stack.pop())
