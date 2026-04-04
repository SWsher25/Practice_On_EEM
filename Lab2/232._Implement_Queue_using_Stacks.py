class MyQueue:

    def __init__(self):
        self.Lstack = []
        self.Rstack = []
        

    def push(self, x: int) -> None:
        self.Rstack.append(x)

    def pop(self) -> int:
        if len(self.Lstack) == 0:
            while len(self.Rstack) > 0:
                self.Lstack.append(self.Rstack.pop())
        return self.Lstack.pop(-1)

    def peek(self) -> int:
        if len(self.Lstack) == 0:
            while len(self.Rstack) > 0:
                self.Lstack.append(self.Rstack.pop())
        return self.Lstack[-1]

    def empty(self) -> bool:
        return len(self.Lstack) == 0 and len(self.Rstack) == 0


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()