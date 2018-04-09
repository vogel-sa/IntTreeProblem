from math import floor
from sys import argv, stderr, stdout

# if len(argv) <= 1 or len(argv) > 2:
#     print >> stderr, "Incorrect number of arguments"
#     exit(-1)
# elif not argv[1].isdigit() and int(argv[0]) <= 0:
#     print >> stderr, "Argument is not a valid tree depth"
#     exit(-1)

# Return a list of the correct size for a binary tree of the given depth
def buildBinTree(depth):
    return [0] * (2**(depth + 1))

# Get the index of the first element at the given depth
def getFirstIndexAtDepth(depth):
    return int(2**(depth)) - 1

# Get the index of the last element at the given depth
def getLastIndexAtDepth(depth):
    return getFirstIndexAtDepth(depth+1) - 1

# return index of parent, or -1 for the root
def getParent(child):
    return int(floor((child - 1)/2))

# Return index of left child
def getLeftChild(parent):
    return 2*parent + 1

# Return index of right child
def getRightChild(parent):
    return 2*parent + 2

# Return index of left neighbor, or -1 if it does not exist
# Always returns -1 if node is not at depth
def getLeftNeighbor(node, depth):
    if getFirstIndexAtDepth(depth) >= node or getLastIndexAtDepth(depth) < node:
        return -1
    else:
        return node - 1

# Return index of right neighbor, or -1 if it does not exist
# Always returns -1 if node is not at depth
def getRightNeighbor(node, depth):
    if getFirstIndexAtDepth(depth) > node or getLastIndexAtDepth(depth) <= node:
        return -1
    else:
        return node + 1

depth = int(argv[1])
tree = buildBinTree(depth)

for d in range(0, depth):
    first = getFirstIndexAtDepth(d)
    last = getLastIndexAtDepth(d)
    for element in range(first, last + 1):
        value = tree[getParent(element)]
        if (d <= 0): # For the root
            tree[element] = 1
        elif element == getLeftChild(getParent(element)): # For the left child
            parentLeftNeighbor = getLeftNeighbor(getParent(element), d-1)
            if parentLeftNeighbor != -1:
                value += tree[parentLeftNeighbor]
            tree[element] = value
        elif element == getRightChild(getParent(element)): # For the right child
            parentRightNeighbor = getRightNeighbor(getParent(element), d-1)
            if parentRightNeighbor != -1:
                value += tree[parentRightNeighbor]
            tree[element] = value
    print tree[first:last+1]
