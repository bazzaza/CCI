
import LinkedListClass as llc


a = llc.LinkedList()
b = llc.LinkedList()

a.insert(9)
a.insert(4)
a.insert(2)
a.insert(1)

b.insert(4)
b.insert(6)
b.insert(5)

a.display()
b.display()

ha = a.head
hb = b.head

def add(ha,hb):

    #ha is head of linked list 'A'
    #hb is head of linked list 'B'


    num1 = 0
    num2 = 0

    #num1 and num2 will store the integer values of linked lists 'A' and 'B'

    node = llc.Node()   #a temp node is created for the linked_list_class
    node.next = ha.next #this temp node is a copy of head of linked list 'A'
    node.data = ha.data

    order = 1       #We start with order = 1, which is the first unit
    while(node):
        num1 += order * node.data  #we add the unit number first, then the tenth place, then the 100th place, etc.
        order = order*10
        node = node.next

    node = llc.Node()   #we repeat the process for list 'B'
    node.next = hb.next
    node.data = hb.data
    order = 1

    while(node):
        num2 += order * node.data
        order = order*10
        node = node.next

    total = num1 + num2 #Now we have the result stored in 'total'


    hc = llc.Node() #we create the head of list 'C'
    hc.data = total%10 #the head stores the 'ones' place
    total = int(total/10) #we then divide by 10

    prev = hc


    while(total):
        node = llc.Node()
        prev.next = node
        node.data = total%10
        total = int(total/10)
        prev = node #this is a pointer.. prev points to node


    return hc


hc = add(ha,hb)

a.display()
b.display()

node = llc.Node()
node.next=  hc.next
node.data = hc.data
s = ""
while(node):
    s += str(node.data) + "->"
    node = node.next

s+="null"
print(s)



