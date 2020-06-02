class queue2Stack:
    def __init__(self):
        self.instack = []
        self.outstack = []

    def insert(self, element):
        self.instack.append(element)

    def dq(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()


s = queue2Stack()
s.insert(1)
s.insert(2)
print(s.dq())
print(s.dq())
