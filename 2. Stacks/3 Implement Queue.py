class queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, *args):
        for i in args:
            self.items.append(i)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self, el=0):
        return self.items[el]


a = queue()
print(a.isEmpty())
a.enqueue(4, 8, 3)
a.enqueue(5, 3)
a.enqueue(6, 7, 8)
a.enqueue(7)
# print(a.peek())

print(a.dequeue())
print(a.dequeue())
print(a.dequeue())
print(a.dequeue())
print(a.dequeue())
print(a.dequeue())
print(a.dequeue())
