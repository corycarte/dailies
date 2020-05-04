def intersection(a, b):  # fill this in.
    testA = a

    while testA:
        testB = b
        while testB:
            if testA.val == testB.val:
                return testA
            else:
                testB = testB.next
        testA = testA.next

    return None



class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    def prettyPrint(self):
        c = self
        while c:
            print("\t" + str(c.val))
            c = c.next

a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next

c = intersection(a, b)
if a:
  print("List A:")
  a.prettyPrint()
if b:
  print("List B:")
  b.prettyPrint()
if c:
  print("List C:")
  c.prettyPrint()
# 3 4