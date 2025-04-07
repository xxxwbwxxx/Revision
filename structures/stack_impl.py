class Stack:
    def __init__(self, size):
        self._size = size
        self.data = [None] * size
        self.avail = 0
    def push(self, item):
        if self.avail >= self._size:
            raise IndexError("Index out of bound!")
        else:
            self.data[self.avail] = item
            self.avail += 1
    def pop(self):
        if self.avail <= 0:
            raise IndexError("Index out of bound!")
        else:
            self.avail -= 1
            popped_item = self.data[self.avail]
            self.data[self.avail] = None
            return popped_item
    def peek(self):
        if self.avail <= 0:
            raise IndexError("Index out of bound!")
        else:
            return self.data[self.avail - 1]
    def is_empty(self):
        return self.avail == 0
    def len(self):
        return self.avail
    

stack = Stack(5)
stack.push(5)
stack.push(10)
print(stack.data)
print(stack.pop())
print(stack.data) 