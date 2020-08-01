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

