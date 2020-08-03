import time
from doubly_linked_list import DoublyLinkedList

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
"""
ORIGINAL NESTED LOOPING RUNTIME: O(n^2) : 5.341 seconds ====================================
"""
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
"""
FIRST TRY INSERTION SORT RUNTIME: O(n^2) : 17.728 seconds ==================================
"""
# sorted_dll = DoublyLinkedList()
# for name in names_1:
#     sorted_dll.sorted_insert(name)
# for name in names_2:
#     sorted_dll.sorted_insert(name)
# current_node = sorted_dll.head.next
# previous_node = sorted_dll.head
# while current_node is not None:
#     if previous_node.value == current_node.value:
#         duplicates.append(current_node.value)
#     current_node = current_node.next
#     previous_node = previous_node.next
"""
SECOND TRY MERGE SORT RUNTIME: O(n log n) : <maximum recursion depth exceeded> =============
"""
# dll = DoublyLinkedList()
# for name in names_1:
#     dll.add_to_head(name)
# for name in names_2:
#     dll.add_to_head(name)
# dll.head = dll.merge_sort(dll.head)
# current_node = dll.head.next
# previous_node = dll.head
# while current_node is not None:
#     if previous_node.value == current_node.value:
#         duplicates.append(current_node.value)
#     current_node = current_node.next
#     previous_node = previous_node.next
"""
NEW RUNTIME: O(n) : 1.020 seconds ==========================================================
"""
# for name_1 in names_1:
#     if name_1 in names_2:
#         duplicates.append(name_1)
"""
BEST RUNTIME: O(n log n) : 0.011 seconds ===================================================

NOTE: List.sort() is always o(n log n). However, this runs faster than the above solution
because merging the lists effectively reduces the value of N by removing recursion.
"""
names_1.extend(names_2)
names_1.sort()
for i in range(1, len(names_1)):
    if names_1[i] == names_1[i-1]:
        duplicates.append(names_1[i])

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish? There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
