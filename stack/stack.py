class Stack:

    def __init__(self, size) -> None:
        self.size = size
        self.stack = []

    def push(self, item) -> None:
        if len(self.stack) < self.size:
            self.stack.append(item)
        else:
            raise Exception("Stack Overflow: The stack is full")

    def pop(self) -> any:
        if len(self.stack):
            return self.stack.pop()
        else:
            raise Exception("Stack Underflow: The stack is empty")

    def peek(self) -> any:
        if len(self.stack):
            return self.stack[-1]
        else:
            raise Exception("Stack Underflow: The stack is empty")
