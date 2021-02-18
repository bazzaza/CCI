class Node:

	def __init__(self, data=None):
		self.data = data
		self.next = None


class LinkedList:

	def __init__(self):
		self.head = None
		self.tail = None


	def insert(self,data):
		this_node = Node(data)

		if not self.head:
			self.head = this_node
			self.tail = this_node
		else:
			this_node.next = self.head
			self.head = this_node


	def append(self,data):
		this_node = Node(data)

		if not self.tail:
			self.tail = this_node
			self.head = this_node
		else:
			self.tail.next = this_node
			self.tail = this_node


	def display(self):
		cur = self.head
		mystr = ""
		cnt = 0
		while(cur and cnt < 20):
			cnt +=1
			mystr += str(cur.data)
			if cur.next:
				mystr += "->"
			else:
				mystr += "->" + "NULL"
			cur = cur.next
		print(mystr)


	def length(self):
		count = 0
		temp = self.head
		while(temp):
			count += 1
			temp = temp.next
		return count



def reverselist(head):

	if not head:
		return head

	prevnode = None

	while(head):
		nextnode = head.next
		head.next = prevnode
		prevnode = head
		head = nextnode

	head = prevnode

	return head

def HasCycle(head):

	if not head:
		return False

	map = {}
	node = Node()
	node.next = head.next

	map[node] = 0

	while(node.next):
		node = node.next
		if node in map:
			return True
		map[node] = 0

	return False






mylist = LinkedList()

mylist.insert(3)
mylist.insert(2)
mylist.insert(1)
mylist.append(4)
mylist.append(5)

# tail = mylist.tail
# tail.next = mylist.head

# tail  = mylist.tail
# tail.next = mylist.head.next.next
# print(tail.next.data)


mylist.display()

x = HasCycle(mylist.head)
print("Has Cycle: " + str(x))




