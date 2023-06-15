# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

    def findTheChild(node: 'TreeNode') -> bool:
        if not node: return False
        print(node.val)
        if node.left or node.right:
            return findTheChild(node.left) or findTheChild(node.right)
        else:
            if node == p or node == q:
                return True
            else:
                return False

    return findTheChild(root)