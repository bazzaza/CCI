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

