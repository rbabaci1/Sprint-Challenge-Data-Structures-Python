# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next


# class LinkedList:
#     def __init__(self):
#         self.head = self.tail = None
#         self.length = 0

#     def add_to_tail(self, value):
#         node = Node(value)
#         if not self.head:
#             self.head = node
#             self.tail = node
#         else:
#             self.tail.next = node
#             self.tail = node
#         self.length += 1


# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.storage = LinkedList()

#     def append(self, item):
#         if self.storage.length < self.capacity:
#             self.storage.add_to_tail(item)
#         else:
#             pass


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.index = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            if self.index == len(self.storage):
                self.index = 0
            self.storage[self.index] = item
        self.index += 1

    def get(self):
        return self.storage

