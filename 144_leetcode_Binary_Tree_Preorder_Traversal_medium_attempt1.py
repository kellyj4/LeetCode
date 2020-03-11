#!/usr/bin/env python3
from typing import List

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Example:
        Input: [1, None, 2, 3]
        1
         \\
          2
         /
        3
        Output: [1, 2, 3]
        """
        preorder_result = []

        if root is None:
            return preorder_result

        preorder_result.append(root.val)

        if root.left is not None:
            preorder_result.extend(self.preorderTraversal(root.left))

        if root.right is not None:
            preorder_result.extend(self.preorderTraversal(root.right))

        if root.left is None and root.right is None:
            return preorder_result

        return preorder_result

#
# Prep work need to create the binary tree structure.
# tree objects 
#
treenode_root = TreeNode(1)
treenode_right = TreeNode(2)

treenode_root.right = treenode_right

treenode_right.left = TreeNode(3)

solution = Solution()
print(solution.preorderTraversal.__doc__)
print("The input is [1, None, 2, 3] the output is => {0}".format(solution.preorderTraversal(treenode_root)))
