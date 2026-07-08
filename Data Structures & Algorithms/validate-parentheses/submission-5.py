class Solution:
    def isValid(self, s: str) -> bool:
        # stack lifo 


        # check for wrong closing parenthesis
        # check if there is no closing parenthesis at all for any opening 
        # 
        stack = []

        for char in s: 
            if char in "({[":
                stack.append(char)
            elif char == ")":
                if not stack or stack.pop() != "(":
                    return False 
            elif char == "}":
                if not stack or stack.pop() != "{":
                    return False
            elif char == "]":
                if not stack or stack.pop() != "[":
                    return False

        return not stack
