# IntTreeProblem
Interview question for Neuroscouting

High level overview:
This script builds a tree of depth N in which any element's value is the sum of its parent's value and its parent's left or right neighbor's value (depending on whether the element is the left or right child). The root is 1.
To create this tree, the script first allocates a list of the correct size to store a binary tree of depth N. Then, it processes the tree in breadth first order, calculating each element's value based on values in the above layer, which have already been calculated.
The script does not need to be compiled (it is in python). In order to run it, simply run the command "python IntTree.py <N>" from the directory containing the IntTree.py file, where <N> is the desired depth of the tree.

Code Organization:
The script is simple, so it is contained in a single file. It first declares the functions required to traverse the tree how we want, such as finding parents and neighbors of elements.
It then creates a an array to hold the tree, iterating over the elements, layer by layer in order to fill the array.

Optimizations:
The tree is stored in breadth-first order as an array. The reason for this is that it makes the most common operations constant-time. For this task, the most common operations are finding parents and neighbors. In a typical node-based implementation of a tree, this requires traversing node links. In the array implementation, these can b calculated in constant time by using math and exploiting the linear layout of data. It is also ideal because the binary tree is completely full, so no space is wasted.