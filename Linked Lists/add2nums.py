
import LinkedListClass as llc


a = llc.LinkedList()
b = llc.LinkedList()

a.insert(3)
a.insert(4)
a.insert(2)

b.insert(4)
b.insert(6)
b.insert(5)

a.display()
b.display()

ha = a.head
hb = b.head

def add(ha,hb):

    num1 = 0
    num2 = 0

    node = llc.Node()
    node.next = ha.next
    node.data = ha.data

    order = 1
    while(node):
        num1 += order * node.data
        order = order*10
        node = node.next

    node = llc.Node()
    node.next = hb.next
    node.data = hb.data
    order = 1

    while(node):
        num2 += order * node.data
        order = order*10
        node = node.next

    total = num1 + num2

    c = llc.LinkedList()

    #assume you can't have insert...


    while(total):
        num = total % 10
        c.append(num)
        total = int(total / 10)

    return c


c = add(ha,hb)

a.display()
b.display()
c.display()


