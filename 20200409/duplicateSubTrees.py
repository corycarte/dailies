class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __repr__(self):
    if self.left and self.right:
      return f"({self.value}, {self.left}, {self.right})"
    if self.left:
      return f"({self.value}, {self.left})"
    if self.right:
      return f"({self.value}, None, {self.right})"
    return f"({self.value})"


def dup_trees(root):
  # Fill this in.
  duplicates = {} # Dictionary to hold results

  # Search Tree in DFS

  stack = []
  stack.append(root)
  
  while stack:
    curr = stack.pop()

    if curr.__repr__() not in duplicates:
      duplicates[curr.__repr__()] = 1
    else:
      duplicates[curr.__repr__()] += 1
    
    if curr.left:
      stack.append(curr.left)
    if curr.right:
      stack.append(curr.right)

  solution = []
  
  for d in duplicates:
    if duplicates[d] > 1:
      temp = []
      for i in range(duplicates[d]):
        temp.append(d)
      solution.append(temp)

  return solution

# I got this wrong. My basic idea was ok. But My function returns
# string representations of the binary trees, not the actual trees.

n3_1 = Node(3)
n2_1 = Node(2, n3_1)
n3_2 = Node(3)
n2_2 = Node(2, n3_2)
n1 = Node(1, n2_1, n2_2)
# Looks like
#     1
#    / \
#   2   2
#  /   /
# 3   3

print(dup_trees(n1))
# [[(3), (3)], [(2, (3)), (2, (3))]]
# There are two duplicate trees
#
#     2
#    /
#   3
# and just the leaf
#
# 3
