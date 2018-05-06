print("Start")
'''print('hello world')

numbers=[10,20,30]
for n in numbers:
	print(n)
'''
class Node:
	'struct node'
	def __init__(self,data):
		self.data=data
		self.nextNode=None
		self.prevNode=None

class LinkedList:
	'Linked list'
	def __init__(self):
		self.head=None
		self.tail=None
		self.size=0
	def inserthead(self,data):
		newNode=Node(data)
		self.size+=1
		newNode.nextNode=self.head
		newNode.nextNode.prevNode=newNode
		self.head=newNode
	def inserttail(self,data):
		newNode=Node(data)
		self.size+=1
		newNode.prevNode=self.tail
		self.tail.nextNode=newNode
		self.tail=newNode
	def print(self):
		tempNode=self.head
		while tempNode is not None:
			print(tempNode.data)
			tempNode=tempNode.nextNode
	def delete(self,data):
		tempNode=self.head
		while tempNode.data != data:
			tempNode=tempNode.nextNode
		tempNode.prevNode.nextNode=tempNode.nextNode
		

list=LinkedList()
x=-1
while x != 0:
	x=int(input("Insert at head"))
	list.inserthead(x)
x=-1
while x != 0:
	x=int(input("Insert at Tail"))
	list.inserttail(x)
list.print()

x=-1
while x != 0:
	x=int(input("Delete element:"))
	list.delete(x)
list.print()


print("End")