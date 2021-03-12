class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def make(self, a,i=0):

        n = len(a)
        if i >= n:
            return None

        if a[i] == None:
            return None

        self.val = a[i]
        self.left = TreeNode().make(a,i=2*i+1)
        self.right = TreeNode().make(a,i=2*i+2)

        return self

    def inOrder(self):

        if self.left:
            self.left.inOrder()

        print(self.val)

        if self.right:
            self.right.inOrder()


a = [15,12,27,7,14,20,88]
# b = [5,1,4,None,None,3,6]
#
root1 = TreeNode().make(a)
# root2 = TreeNode().make(b)
#
root1.inOrder()
print("#######")
#print("Tree Created!")

c  = [6,2,8,1,3,7,9]
root = TreeNode().make(c)
root.inOrder()