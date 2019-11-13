# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:    
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
