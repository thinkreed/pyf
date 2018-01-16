class Queue:
    def __init__(self, head=None):
        self.storage = [head]
        self.head = head

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        return self.storage.pop(0)
