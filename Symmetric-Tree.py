# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# Iterative Solution
class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        else:
            stack = [[root.left, root.right]]

        while stack:
            left, right = stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.insert(0, [left.left, right.right])
                stack.insert(0, [left.right, right.left])
            else:
                return False
        return True

lefetleftnode = TreeNode(3,None,None)
rightrightnode = TreeNode(3,None,None)
rightleftnode = TreeNode(4,None,None)
leftrightnode = TreeNode(4,None,None)

leftnode = TreeNode(2,lefetleftnode,leftrightnode)
rightnode = TreeNode(2,rightleftnode,rightrightnode)
roottnode = TreeNode(2,leftnode,rightnode)
test = Solution()
print(test.isSymmetric(roottnode))