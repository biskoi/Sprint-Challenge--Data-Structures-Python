class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next_node
            # current.next = prev     doesn't work for some reason
            current.set_next(prev)
            prev = current
            current = next_node
        self.head = prev


# myll = LinkedList()
# myll.add_to_head(1)
# myll.add_to_head(2)
# myll.add_to_head(3)
# myll.add_to_head(4)
# myll.add_to_head(5)
# print(myll.head.value)
# myll.reverse_list(myll.head, None)
# print(myll.head.value)
