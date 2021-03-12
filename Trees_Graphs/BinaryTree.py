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



a = [15,12,27,7,14,28,88]
b = [5,1,4,None,None,3,6]

root1 = TreeNode().make(a)
root2 = TreeNode().make(b)

print("Done")