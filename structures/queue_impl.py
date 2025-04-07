from collections import deque

class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if not self._data:
            raise IndexError("Index out of range!")
        return self._data.popleft()

    def is_empty(self):
        return len(self._data) == 0


    def peek(self):
        if self.is_empty():
            raise IndexError("Index out of range!")
        return self._data[0]
    def __len__(self):
        return len(self._data)
    
queue = Queue()
queue.enqueue(10)
queue.enqueue(5)
queue.enqueue(1)
print(queue._data)
print(queue.dequeue())
print(queue.peek())
print(queue._data)
