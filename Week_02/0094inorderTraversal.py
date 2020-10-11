# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result, stack = [], [(root, False)]

        while stack:
            curr, flag = stack.pop()
            if curr:
                if flag:
                    result.append(curr.val)
                else:
                    stack.append((curr.right, False))
                    stack.append((curr, True))
                    stack.append((curr.left, False))
        return result