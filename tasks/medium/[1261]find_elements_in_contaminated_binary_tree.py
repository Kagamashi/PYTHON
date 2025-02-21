'''
[1261][Find Elements in a Contaminated Binary Tree]
Given binary tree with following rules:
1. root.val == 0
2. for any treeNode:
    1. if treeNode.val has a value x and treeNode.left != null, then treeNode.left.val == 2*x+1
    2. if treeNode.val has a value x and treeNode.right != null, then treeNode.right.val == 2*x+2

Now binary tree is contaminated which means all treeNode.val have been changed to -1

Implement FindElements class:
- FindElements(TreeNode* root) initializes the object with contaminated binary tree and recovers it
- bool find(int target) returns true if target value exists in recovered binary tree

[Solution]
- Depth-First Search (DFS) used to traverse and restore the tree efficiently
- Set is used for fast lookups - restored values are stored in a set allowing O(1) average-time complexity for find() operations
'''

from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class FindElements:
    def __init__(self, root: TreeNode):
        self.values = set() # set storing all valid values
        if root:
            self.recover(root)  # if root is not None it calls recover() with val=0 to reconstruct the tree

    def recover(self, root: TreeNode):
        queue = deque([(root, 0)])
        while queue:
            node, val = queue.popleft() 
            node.val = val # assign correct value to the node
            self.values.add(val) # add value to self.values
            if node.left:
                queue.append((node.left, 2 * val + 1))
            if node.right:
                queue.append((node.right, 2 * val + 2))
    
    def find(self, target: int) -> bool: # checks if target is in self.value
        return target in self.values

'''
Example step-by-step guide
        -1
       /  \
     -1    -1
    /  \     \
  -1   -1    -1

Step 1: reconstructing the Tree with 
      0     # root is initialized with 0
     /  \
   -1    -1
  /  \     \
-1   -1    -1

# left child is set to 2 * 0 + 1 = 1, and the right child is set to 2 * 0 + 2 = 2
      0
     /  \
    1    2
  /  \     \
-1   -1    -1

# left child of 1 is 2 * 1 + 1 = 3, and the right child is 2 * 1 + 2 = 4:
      0
     /  \
    1    2
  /  \     \
 3    4    -1

# right child of 2 is 2 * 2 + 2 = 6:
        0
       /  \
      1    2
    /  \     \
   3    4     6

values set now contains {0, 1, 2, 3, 4, 6}

Step 2: finding values (find method)
find(3)     true        3 is in the restored tree
'''