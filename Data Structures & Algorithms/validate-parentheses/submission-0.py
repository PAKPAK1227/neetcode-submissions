class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if not stack:
                    return False
                character = stack.pop()
                if c == ")" and character != "(":
                    return False
                elif c == "}" and character != "{":
                    return False
                elif c == "]" and character != "[":
                    return False
        
        if not stack:
            return True
        else:
            return False

