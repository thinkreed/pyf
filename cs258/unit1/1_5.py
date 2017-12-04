import array
import random


class Queue:
    def __init__(self, size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self, x):
        if self.size == self.max:
            return False

        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0
        return True

    def dequeue(self):
        if self.size == 0:
            return None
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x


def test():
    q = Queue(2)
    c1 = q.enqueue(6)
    c2 = q.enqueue(7)
    c3 = q.enqueue(8)
    c4 = q.dequeue()
    c5 = q.dequeue()
    c6 = q.dequeue()

    print c1, c2, c3, c4, c5, c6


test()
