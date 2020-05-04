class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def MinVal(root_node):
    nxt = root_node
    while nxt.left != None:
        nxt = nxt.left

    return nxt.value

def MaxVal(root_node):
    nxt = root_node
    while nxt.right != None:
        nxt = nxt.right

    return nxt.value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
    stk = list()
    floor = MinVal(root_node)
    ceil = MaxVal(root_node)
    
    stk.append(root_node)
    found = False
    while len(stk) > 0 and not found:
        nxt = stk.pop()
        if nxt.left != None:
            stk.append(nxt.left)
        if nxt.right != None:
            stk.append(nxt.right)

        if nxt.value == k:
            floor = ceil = nxt.value
            return floor, ceil
        elif nxt.value < k:
            floor = max(floor, nxt.value)
        elif nxt.value > k:
            ceil = min(ceil, nxt.value)

    if floor == k and not found or ceil == k and not found:
        return None, None
    else:
        return floor, ceil




root = Node(8)
root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)

print(findCeilingFloor(root, 5))
# (4, 6)
print(findCeilingFloor(root, 12))
# (12, 12)
print(findCeilingFloor(root, 13))
# (12, 14)