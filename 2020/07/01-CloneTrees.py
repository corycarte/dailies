class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def findNode(a, b, node):
  # Fill this in.
  if a == node:
    return b
  if a.left and b.left:
    found = findNode(a.left, b.left, node)
    if found:
      return found
  if a.right and b.right:
    found = findNode(a.right, b.right, node)
    if found:
      return found
  return None

def findNode2(a, b, node):
  stack = [(a, b)]
  
  while len(stack):
    (a, b) = stack.pop()
    if a == node:
      return b
    if a.left and b.left:
      stack.append((a.left, b.left))
    if a.right and b.right:
      stack.append((a.right, b.right))
  return None

#  1
# / \
#2   3
#   / \
#  4*  5


a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.right.left = Node(4)
a.right.right = Node(5)

b = Node(1)
b.left = Node(2)
b.right = Node(3)
b.right.left = Node(4)
b.right.right = Node(5)

found1 = findNode(a, b, a.right.left)
# 4
if found1:
  print(found1.val)
else:
  print("No node found")

found2 = findNode2(a, b, a.right.left)
if found2:
  print(found2.val)
else:
  print("No node found")