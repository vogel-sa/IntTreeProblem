Definitions
- neighbor: The node directly to the left or right on the same level as a certain node.

Problem:
Build a tree of integers which has the following properties:
- The root node has value 1.
- Each node in the tree has two children.
- The value for the children nodes is determined as follows:
-- If it's the left children, its value will be the sum of the parent's value and the parent's left neighbor's value. If the parent has no left neighbor, then the child's value is the same as its parent.
-- If it's the right children, its value will be the sum of the parent's value and the parent's right neighbor's value. If the parent has no right neighbor, then the child's value is the same as its parent.

The program should be able to accept an input value to determine how many levels of this tree it should generate. How the program receives the input value is up to you (for example it could be in the command line, reading a file, with some GUI, anything really). The program should build the tree and then print it out. Again, how you print it is completely up to you (it could print to a file, on the console, on a window, anything!).

Here are a couple of example trees for different input values (apologies in advance for the ASCII art!):
Input value: 1
Tree should be:
1 (just the root of the tree)

Input value: 2
Tree should be:
  1
 / \
 1  1 (Since the root doesn't have any neighbors both left and right child get the root's value)

Input value: 4
Tree should be:
          1
     /         \
    1           1
  /   \       /   \
 1     2     2     1
/ \   / \   / \   / \
1 3   3 4   4 3   3 1

You can use any programming language you want.

For your submission, we'd like to get a zipped git repository that includes the code for the script (you can break it up in multiple files if you want to) along with a README file that contains:
- Description of how script works at a high-level, and how to compile it and run it.
- How the code is organized (which modules do what, and their external dependencies)
  and how control flows through the script.
- Interesting optimizations (if any)

The purpose of getting the git repository is we'd like to see how you work through a project. We're big believers of commit early, commit often, and also  good commit messages, and getting a glimpse into the commit history that you did in creating this project is very valuable to this interview.

And don't worry if you have simple commits like "fix typo" or "deleted the wrong files", or commits where you were testing things out or getting familiar with some python package, our repositories are full of those (and even more embarrassing things!)
