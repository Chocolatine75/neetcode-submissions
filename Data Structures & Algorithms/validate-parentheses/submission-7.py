class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for parent in s:

            if parent == ")" or parent == "]" or parent == "}":
                if stack == []:
                    return False
                left = stack.pop()
                if parent == "}":
                    if left != "{":
                        return False
                if parent == "]":
                    if left != "[":
                        return False
                if parent == ")":
                    if left != "(":
                        return False
            else:
                stack.append(parent)
        
        if len(stack)>0:
            return False
        return True

        