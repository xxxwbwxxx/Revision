class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_by_value(self, value):
        if not self.head:
            return
        if self.head.data == value:
            self.head = self.head.next
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next
        
    def display(self):
        current = self.head
        while current.next:
            print(current.data, end=" > ")
            current = current.next
        print(current.data, " > ", end=" None \n")
        print()

    def reverse(self):
        current = self.head
        prev = None
        while current.next:
            temp_next = current.next
            current.next = prev
            prev = current
            current = temp_next
        self.head = prev

test = SinglyLinkedList()
test.append(1)
test.append(2)
test.append(3)
test.append(4)
test.display()
test.append(6)
test.display()
test.delete_by_value(6)
test.display()
test.insert_at_beginning(0)
test.display()
test.reverse()
test.display()
