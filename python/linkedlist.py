import sys #for write
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
	def insertHead(self,data):
		newNode=Node(data)
		newNode.nextNode=self.head
		if newNode.nextNode is not None:
			newNode.nextNode.prevNode=newNode
		else:
			self.tail=newNode
		self.head=newNode
	def insertTail(self,data):
		newNode=Node(data)
		newNode.prevNode=self.tail
		if newNode.prevNode is not None:
			newNode.prevNode.nextNode=newNode
		else:
			self.head=newNode
		self.tail=newNode
	def printHead(self):
		tempNode=self.head
		while tempNode is not None:
			sys.stdout.write(tempNode.data)
			tempNode=tempNode.nextNode
		print("")
	def printTail(self):
		tempNode=self.tail
		while tempNode is not None:
			sys.stdout.write(tempNode.data)
			tempNode=tempNode.prevNode
		print("")
	def delete(self,data):
		tempNode=self.head
		while tempNode.data != data:
			tempNode=tempNode.nextNode
		tempNode.prevNode.nextNode=tempNode.nextNode
		tempNode.nextNode.prevNode=tempNode.prevNode
	def deleteHead(self):
		self.head=self.head.nextNode
		self.head.prevNode=None
	def deleteTail(self):
		self.tail=self.tail.prevNode
		self.tail.nextNode=None

		
list=LinkedList()
print("0:exit")
print("1.insertHead")
print("2.insertTail")
print("3.printHead")
print("4.printTail")
print("5.delete")
print("6.deleteHead")
print("7.deleteTail")

while True:
	x=int(input("Enter Choice:"))
	if x==0:
		break
	elif x==1:
		list.insertHead(input())
	elif x==2:
		list.insertTail(input())
	elif x==3:
		list.printHead()
	elif x==4:
		list.printTail()
	elif x==5:
		list.delete(input())
	elif x==6:
		list.deleteHead()
	elif x==7:
		list.deleteTail()
	else:
		print("0:exit")
		print("1.insertHead")
		print("2.insertTail")
		print("3.printHead")
		print("4.printTail")
		print("5.delete")
		print("6.deleteHead")
		print("7.deleteTail")




print("Gracefully exited")