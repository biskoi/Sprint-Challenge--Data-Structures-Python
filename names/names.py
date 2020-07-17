import time
import os
from binary_search_tree import BSTNode
from singly_linked_list import LinkedList

start_time = time.time()

f = open(f'{os.getcwd()}\\names\\names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open(f'{os.getcwd()}\\names\\names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# bst_1 = BSTNode(None)
# ll_1 = LinkedList()
# ll_2 = LinkedList()

# for names in names_1:
#     ll_1.add_to_tail(names)

# for names in names_2:
#     ll_2.add_to_tail(names)

# item = ll_1.head

# while item:
#     # print(item)
#     if ll_2.contains(item.value):
#         duplicates.append(item.value)
#     item = item.next_node

bst_1 = BSTNode('init')
bst_2 = BSTNode('INIT')

for names in names_1:
    bst_1.insert(names)
for names in names_2:
    bst_2.insert(names)

def find_dupes(str):
    if bst_2.contains(str):
        duplicates.append(str)

bst_1.for_each(find_dupes)



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
