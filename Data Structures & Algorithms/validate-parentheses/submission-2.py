class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        for c in s:
            if c == '{' or c == "(" or c == "[":
                stack.append(c)
            elif c == '}':
                if len(stack) == 0:
                    return False
                open_paren = stack.pop()
                if open_paren != '{':
                    return False
            elif c == ')':
                if len(stack) == 0:
                    return False
                open_paren = stack.pop()
                if open_paren != '(':
                    return False
            else:
                if len(stack) == 0:
                    return False
                open_paren = stack.pop()
                if open_paren != '[':
                    return False
        
        if len(stack) != 0:
            return False
        
        return True
        


            

            
