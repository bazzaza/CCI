from Trees.BinaryTree import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
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

        def invertList(l):
            left = 0
            right = len(l) -1

            while(left < right):
                l[left],l[right]=l[right],l[left]
                left+=1
                right-=1

        for i in range(len(levels)):
            if i%2==1:
                invertList(levels[i])

        return levels




if __name__ == '__main__':

    root = [3, 9, 20, None, None, 15, 7]
    root = [1,2,3,4,None,None,5]
    root = TreeNode().make(root)
    ans = Solution().zigzagLevelOrder(root)
    print(ans)
