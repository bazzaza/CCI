from Trees.BinaryTree import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level = 0
        levels = []

        def traverse(node,level=0,levels=[]):

            if node != None:
                if(level == len(levels)):
                    levels.append([])


                levels[level].append(node.val)

                level += 1
                traverse(node.left,level=level,levels=levels)
                traverse(node.right,level=level,levels=levels)

        traverse(root,level=level,levels=levels)
        return levels




if __name__ == '__main__':

    root = [3, 9, 20, None, None, 15, 7]
    root = TreeNode().make(root)
    ans = Solution().levelOrder(root)
    print(ans)
