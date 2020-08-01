# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next


# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0

#     def add_to_tail(self, value):  # O(1)
#         new_node = Node(value)
#         if self.tail:
#             self.tail.next = new_node
#             self.tail = new_node
#         else:
#             self.head = new_node
#             self.tail = new_node
#         self.length += 1


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.location = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
            self.location += 1
        else:
            if self.location == len(self.storage):
                self.location = 0
            self.storage.pop(self.location)
            self.storage.insert(self.location, item)
            self.location += 1

    def get(self):
        return self.storage

