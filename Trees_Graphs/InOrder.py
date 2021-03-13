from Trees.BinaryTree import TreeNode

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        a = []
        if root == None:
            return a

        def helper(root,a):

            if root.left:
                helper(root.left,a)

            a.append(root.val)

            if root.right:
                helper(root.right,a)

        helper(root,a)
        return a



# root = [1,2]
root = [1,2,3,4,5,6,7,8]
root = TreeNode().make(root)
solution = Solution().inorderTraversal(root)
print(solution)