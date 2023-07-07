class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        if not root.left and not root.right:
            # Check if the current node is a leaf node
            return root.val == targetSum

        # Recursively check if the target sum can be reached in the left or right subtree
        return (
            self.hasPathSum(root.left, targetSum - root.val)
            or self.hasPathSum(root.right, targetSum - root.val)
        )
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

targetSum = 22

solution = Solution()
print(solution.hasPathSum(root, targetSum))
