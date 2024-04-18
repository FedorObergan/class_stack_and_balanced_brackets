class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, elem):
        self.items.append(elem)

    def pop(self):
        if self.is_empty():
            raise Exception('pop() called on empty stack')
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception('peek() called on empty stack')
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
