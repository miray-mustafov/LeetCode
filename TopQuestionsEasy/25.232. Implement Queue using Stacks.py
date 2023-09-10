class MyQueue:

    def __init__(self):
        self.q = []
        self.helper = []

    def push(self, x: int) -> None:
        while self.q:
            self.helper.append(self.q.pop())
        self.q.append(x)
        while self.helper:
            self.q.append(self.helper.pop())

    def pop(self):
        return self.q.pop()

    def peek(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0


mq = MyQueue()
mq.push(1)
mq.push(2)
mq.push(3)
print(mq.pop())
mq.push(4)
print(mq.pop())

