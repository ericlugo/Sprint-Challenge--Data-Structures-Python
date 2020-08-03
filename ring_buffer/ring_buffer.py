class BufferNode:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = BufferNode()
        self.write_head = self.head
        
        current_node = self.head
        for value in range(self.capacity-1):
            current_node.next = BufferNode()
            current_node = current_node.next
            if value == self.capacity-2:
                current_node.next = self.head
                
    def append(self, item):
        self.write_head.value = item
        self.write_head = self.write_head.next

    def get(self):
        current_content = []
        current_node = self.head
        for _ in range(self.capacity):
            if current_node.value is not None:
                current_content.append(current_node.value)
            current_node = current_node.next
        return current_content