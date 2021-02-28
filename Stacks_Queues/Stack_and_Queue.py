from collections import deque

#Stacks are useful for recursion, for implementing 'undo' fucntion in some software
#and in storing the browsing history, so when you click 'back', the last visited website is
#'popped' from the stack

#while python lists can be used to implement stacks, it is more space efficient to use
#deque from collections. Deque is a generalized queue, where you can add and remove items
#from either side of the queue. It is implemented using a doubly linked list

class Stack:

    def __init__(self):
        self.container = deque()

    def push(self, x):
        self.container.append(x)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def isEmpty(self):
        return len(self.container) ==0

    def size(self):
        return len(self.container)

    def display(self):
        print(self.container)

class Queue:

    def __init__(self):
        self.container = deque()

    def add(self, x):
        self.container.appendleft(x)

    def remove(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def isEmpty(self):
        return len(self.container) == 0

    def count(self):
        return len(self.container)

    def display(self):
        print(self.container)