class Stack:


    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit
        

    def isEmpty(self):
        if self.items:
            return False
        else:
            return True


    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            return None

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return None

    def peek(self):
        if len(self.items) > 0:
            return self.items[len(self.items)-1]
        else:
            return None
    
    def size(self):
        return len(self.items)


    def full(self):
        if len(self.items) < self.limit:
            return False
        else:
            return True

    def search(self, target):
        if target in self.items:
            return (len(self.items)-1) - self.items.index(target, 0, len(self.items))
        else:
            return -1
