from queue import Queue
from stack import Stack

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #val is less than self.val
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            #if left child == none, insert val into self.left
            else:
            #else repeat op on existing left subtree
                self.left.insert(value)
        #val is equal or more than self.val
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #case 1: self.value == target
        if self.value == target:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        elif target >= self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        else: 
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        max_val = self.value
        current = self
        while current.right is not None:
            max_val = current.right.value
            current = current.right
        return max_val


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right is not None:
            # self.right.for_each(self.right.value)
            self.right.for_each(fn)
        if self.left is not None:
            # self.left.for_each(self.left.value)
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        #if current = none
            #theres nothing else to look at, return
        #if self.left
            #go left, recurse on self.left
        if self is None:
            return
        
        if self.left is not None:
            self.left.in_order_print(self)
        # ^^^^ Recursion here, keeps on going left in BST until it cant anymore, and THEN prints as it's exiting

        print(self.value) # this is IN ORDER because the print/visit is in the middle of checking left and right. pre-order would be printing right away, then checking left and right

        #after printing, check if we can go right - if we can, recurse on it, and function will keep going left until it can't anymore again
        if self.right is not None:
            self.right.in_order_print(self)

        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):

        value_queue = Queue()
        value_queue.enqueue(self)
        #can use a queue data structure to form a "line"
        #place root in queue

        #need a while loop to iterate, checking if queue is greater than 0
            #dequeue item from front of queue, print it
            #place current's left node in queue if not none
            #place current's right node in queue if not none

        while value_queue.size > 0:
            current = value_queue.dequeue()
            print(current.value)
            if current.left is not None:
                value_queue.enqueue(current.left)
            if current.right is not None:
                value_queue.enqueue(current.right)




    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):

        #needs while loop for iteration, checking if stack is empty
            #print the top item, popping it off
            #if left, push left item's value onto stack
            #if right, push right onto stack
            ##Because of how STACKS work, if we deal with right last, it will end up on top, and printing before the left value which is beneath it in the stack. To print left first, we need to deal with left LAST

        val_stack = Stack()
        val_stack.push(node)

        while val_stack.size > 0:
            current = val_stack.pop()
            print(current.value)
            if current.right is not None:
                val_stack.push(current.right)
            if current.left is not None:
                val_stack.push(current.left)

    # Stretch Goals ------------------------- 
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

# bst = BSTNode(1)
# bst.insert(2)
# bst.insert(3)
# bst.insert(4)
# bst.insert(5)
# bst.insert(6)
# bst.insert(7)
# bst.insert(8)

# # bst.in_order_print(bst)
# bst.bft_print(bst)
# bst.dft_print(bst)