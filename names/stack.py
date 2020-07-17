import os
from singly_linked_list import LinkedList 

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         if len(self.storage) != 0:
#             return self.storage.pop()
#         else:
#             return None

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        if self.storage.head == None:
            return 0
        elif self.storage.head:
            current = self.storage.head
            length = 0
            while current:
                length += 1
                current = current.next_node if current.next_node else False
            return length

    def push(self, value):
        # if self.storage.head is None:
        #     self.storage.head = Node(value)
        # else:
        #     current = self.storage.head
        #     while current.get_next()
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.storage.remove_tail()



