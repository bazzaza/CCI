from Trees.BinaryTree import TreeNode


class Solution(object):
    def isValidBST(self, root):
        """
            :type root: TreeNode
            :rtype: bool
                """

        def inOrder(root, a):
            if root.left:
                temp = inOrder(root.left, a)
                if temp == False:
                    return False

            if root.val <= a[-1]:
                return False
            else:
                a.append(root.val)

            if root.right:
                temp = inOrder(root.right, a)
                if temp == False:
                    return False


        min = float('-inf')
        a = [min]

        result = inOrder(root,a)

        if result == None:
            return True
        else:
            return result




root = [2,1,3]
root = [5,1,4,None,None,3,6]
root = [1,1]
root = TreeNode().make(root)

solution = Solution().isValidBST(root)
print(solution)



#In a Binary Search Tree (BST), all keys in left subtree of a key must be smaller
# and all keys in right subtree must be greater.
# So a Binary Search Tree by definition has distinct keys and duplicates in binary search tree are not allowed.