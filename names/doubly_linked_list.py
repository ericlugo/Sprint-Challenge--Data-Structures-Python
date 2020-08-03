import math
from dll_node import DLL_Node


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    def merge(self, first, second):
        if first is None:
            return second
        if second is None:
            return first
        if first.value < second.value: 
            first.next = self.merge(first.next, second) 
            first.next.prev = first 
            first.prev = None   
            return first 
        else: 
            second.next = self.merge(first, second.next) 
            second.next.prev = second 
            second.prev = None
            return second
    
    def merge_sort(self, head): 
        if head is None:  
            return head 
        if head.next is None: 
            return head 
        second = self.split(head) 
        head = self.merge_sort(head) 
        second = self.merge_sort(second) 
        return self.merge(head, second) 
    
    def split(self, head): 
        fast = head
        slow = head 
        while(True): 
            if fast.next is None: 
                break
            if fast.next.next is None: 
                break
            fast = fast.next.next 
            slow = slow.next
        temp = slow.next
        slow.next = None
        return temp 
    
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

    def remove_from_head(self):
        if self.length == 0:
            return None
        else:
            deleted_node_value = self.head.value
            self.delete(self.head)
            return deleted_node_value

    def remove_from_tail(self):
        if self.length == 0:
            return None
        else:
            deleted_node_value = self.tail.value
            self.delete(self.tail)
            return deleted_node_value

    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)

    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    def delete(self, node):
        if self.length == 0:
            return None
        else:
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                if node == self.head:
                    self.head = node.next
                elif node == self.tail:
                    self.tail = node.prev
                node.delete()
        self.length -= 1

    def get_max(self):
        left_pointer = self.head
        right_pointer = self.tail
        highest_value = self.head.value if self.head else None
        if self.length != 0:
            for _ in range(math.ceil(self.length/2)):
                if highest_value < left_pointer.value:
                    highest_value = left_pointer.value
                if highest_value < right_pointer.value:
                    highest_value = right_pointer.value
                left_pointer = left_pointer.next
                right_pointer = right_pointer.prev
        return highest_value

    def get_middle(self):
        middle = self.head
        end = self.head
        while end.next != None and end.next.next != None:
            end = end.next.next
            middle = middle.next
        if self.length % 2 == 0:
            return [middle.value, middle.next.value]
        else:
            return [middle.value]

    def get_list(self):
        linked_list_values = []
        current_node = self.head
        while current_node is not None:
            linked_list_values.append(current_node.value)
            current_node = current_node.next
        return linked_list_values

    def contains(self, value):
        match_found = False
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                match_found = True
            current_node = current_node.next
        return match_found

    def reverse(self):
        iterator = self.head
        current_node = self.head
        while iterator is not None:
            iterator = iterator.next
            current_node.next = current_node.prev
            current_node.prev = iterator
            current_node = iterator
        self.head = self.tail
        self.tail = iterator


# testing the list
# myList = DoublyLinkedList()
# myList.add_to_head(1)
# myList.add_to_head(0)
# myList.add_to_tail(2)
# myList.add_to_tail(3)
# myList.add_to_head(10)
# myList.add_to_head(15)
# myList.add_to_head(-1)
# print(myList.get_list())
# print(myList.get_max())
# print(myList.get_middle())
# print(myList.contains(10))
# myList.reverse()
# print(myList.get_list())
