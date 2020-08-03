# import math
from dll_node import DLL_Node


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    For a MergeSort we will need three functions:
    merge(), merge_sort(), and split()
    
    merge() should:
    - if only one list is received, return it as is
    - if both lists are received, compare the value of each head
        recursively merge in order
    merge_sort() should:
    - if unable to split the list due to size return the list
    - create pointer to second half and sever the connection to first half
    - recursively continue to split until we have single item "lists"
    - as the splitting terminates, begin to re-form the connections
    split() should:
    - initiate pointers
    - find last node of the first half of linked list
    - create pointer to the start of the second half of linked list
    - cut off second half of linked list
    - return second half's head
    """
    
    def merge(self, first_half, second_half):
        if first_half is None:
            return second_half
        if second_half is None:
            return first_half
        
        if first_half.value < second_half.value: 
            first_half.next = self.merge(first_half.next, second_half) 
            first_half.next.prev = first_half 
            first_half.prev = None   
            return first_half 
        else: 
            second_half.next = self.merge(first_half, second_half.next) 
            second_half.next.prev = second_half 
            second_half.prev = None
            return second_half
    
    def merge_sort(self, head):
        if (head is None) or (head.next is None): 
            return head 
        split_head = self.split(head) 
        head = self.merge_sort(head) 
        split_head = self.merge_sort(split_head)
        return self.merge(head, split_head) 
    
    def split(self, head): 
        fast_pointer = head
        mid_pointer = head 
        while (fast_pointer.next is not None) and (fast_pointer.next.next is not None): 
            fast_pointer = fast_pointer.next.next 
            mid_pointer = mid_pointer.next
        split_head = mid_pointer.next
        mid_pointer.next = None
        return split_head
    
    """
    For an Insertion Sort we will need one function:
    sorted_insert()
    
    sorted_insert() should:
    - instantiate a new node if none currently exists
    - call add_to_head() if the value received is smaller than the current head
    - iterate through list to find greatest value below new value for insertion point
    - increase length of dll
    """
    
    def sorted_insert(self, value):
        if self.length == 0:
            new_node = DLL_Node(value)
            self.head = new_node
            self.tail = new_node
        elif value < self.head.value:
            self.add_to_head(value)
        else:
            current_node = self.head
            while current_node.next is not None and current_node.next.value < value:
                current_node = current_node.next
            if current_node == self.tail:
                self.add_to_tail(value)
            else:
                current_node.insert_after(value)
        self.length += 1

    def add_to_head(self, value):
        if self.length == 0:
            new_node = DLL_Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.head.insert_before(value)
            self.head = self.head.prev
        self.length += 1

    def add_to_tail(self, value):
        if self.length == 0:
            new_node = DLL_Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        self.length += 1

    def contains(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False