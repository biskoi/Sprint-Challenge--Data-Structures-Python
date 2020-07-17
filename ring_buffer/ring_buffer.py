from singly_linked_list import Node
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0 
        self.storage = [None] * capacity
        # self.head = None
        self.pointer = 0

    def append(self, item):
        # if self.head is None:
        #     self.head = Node(item, item)
        #     self.pointer = self.head
        #     self.size += 1
        # elif self.size < self.capacity:
        #     self.pointer.set_next(Node(item, self.head))
        #     self.pointer = self.head.get_next()
        #     self.size += 1
        # elif self.size == self.capacity:
        #     self.pointer.set_next(Node(item, ))
        if self.pointer == self.capacity:
            self.pointer = 0

        self.storage[self.pointer] = item
        self.pointer += 1



    def get(self):
        return [item for item in self.storage if item is not None]