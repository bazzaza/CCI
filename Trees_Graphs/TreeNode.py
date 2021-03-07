class TreeNode:
    def __init__(self, data = "NA"):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def display(self, space = ""):
        #if len(space) > 3:

        print(space + self.data)
        if self.children:
            space = space[:-2] + "  |__"
            for child in self.children:
                child.display(space)


a = TreeNode("Electronics")
b = TreeNode("Video Games")
b1 = TreeNode("Nintendo")
b2 = TreeNode("Xbox")
b3 = TreeNode("Playstation")

c = TreeNode("Mobile Phones")
c1 = TreeNode("Apple")
c2 = TreeNode("Samsung")
c11 = TreeNode("Iphone 7")

d = TreeNode("Laptops")
d1 = TreeNode("Lenovo")
d2 = TreeNode("Dell")
d11 = TreeNode("Thinkpad")
d21 = TreeNode("AlienWare")

a.add_child(b)
a.add_child(c)
a.add_child(d)
b.add_child(b1)
b.add_child(b2)
b.add_child(b3)

c.add_child(c1)
c.add_child(c2)
c1.add_child(c11)

d.add_child(d1)
d.add_child(d2)
d1.add_child(d11)
d2.add_child(d21)

a.display()