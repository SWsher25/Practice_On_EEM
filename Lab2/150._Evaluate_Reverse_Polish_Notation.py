class Solution:
    def evalRPN(tokens) -> int:
        stack = []

        for i in tokens:
            if i.isdecimal():
                stack.append(i)
            else:
                if len(i) > 1 and "-" in i:
                    i = int(i)
                    stack.append(i)
                elif i == "+":
                    stack.append(int(stack.pop(-2)) + int(stack.pop(-1)))
                elif i == "-":
                    stack.append(int(stack.pop(-2)) - int(stack.pop(-1)))
                elif i == "*":
                    stack.append(int(stack.pop(-2)) * int(stack.pop(-1)))
                else:
                    stack.append(int(stack.pop(-2)) / int(stack.pop(-1)))

        return stack[-1]
    
    print(evalRPN(tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))