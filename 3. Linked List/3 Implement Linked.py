class singlyLinked(object):
    def __init__(self,value):
        self.value=value
        self.nextnode=None

a = singlyLinked(1)
b = singlyLinked(2)
c = singlyLinked(3)

a.nextnode=b
b.nextnode=c
print(a.nextnode.value)

class doublyLinked(object):
    def __init__(self,value):
        self.value=value
        self.nextnode=None
        self.prevnode=None

a = doublyLinked(1)
b = doublyLinked(2)
c = doublyLinked(3)

a.nextnode=b
b.nextnode=c

c.prevnode=b
b.prevnode=a

print(b.prevnode.value)
print(b.nextnode.value)