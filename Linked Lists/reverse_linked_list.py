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
		while(cur):
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

	a = []

	tnode = Node()
	tnode.data = head.data
	tnode.next = head.next

	while(tnode):
		a.append(tnode.data)
		tnode = tnode.next

	tnode = Node()
	tnode.data = head.data
	tnode.next = head.next

	head.data = a.pop()
	tnode = tnode.next

	while(tnode):
		tnode.data = a.pop()
		tnode = tnode.next

	head.data
	return head


mylist = LinkedList()

mylist.insert(10)
mylist.insert(20)
mylist.insert(14)
mylist.append(99)



mylist.display()

mylist.head = reverselist(mylist.head)

mylist.display()




