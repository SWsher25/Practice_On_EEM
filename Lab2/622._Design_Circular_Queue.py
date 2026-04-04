class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.q = [0] * k
        self.head = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        tail = (self.head + self.size) % self.k
        self.q[tail] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.head = (self.head + 1) % self.k
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.head + self.size - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k