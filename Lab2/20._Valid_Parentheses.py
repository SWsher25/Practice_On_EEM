class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        op = ["(", "[", "{"]
        cl = [")", "]", "}"]

        for i in range(len(s)):
            if s[i] in op:
                stack.append(s[i])
            else:
                if len(stack) != 0 and op.index(stack[-1]) == cl.index(s[i]):
                    stack.pop(-1)
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
