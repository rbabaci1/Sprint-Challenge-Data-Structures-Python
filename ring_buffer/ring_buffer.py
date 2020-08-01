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
            self.storage.pop(self.index)
            self.storage.insert(self.index, item)
        self.index += 1

    def get(self):
        return self.storage

