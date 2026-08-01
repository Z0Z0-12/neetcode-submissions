class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        matching = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        for i in s:
            if i in matching:
                if not stack:
                    return False
                
                if stack[-1] == matching[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        if stack == []:
            return True
        else:
            return False


                