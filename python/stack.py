class Stack:
	def __init__(self):
		self.stack=[]
	def isEmpty(self):
		return self.stack==[]
	def push(self,data):
		self.stack.append(data)
	def pop(self):
		if self.isEmpty==True:
			print("Stack Empty")
			return
		data=self.stack[-1]
		del self.stack[-1]
		return data
	def peek(self):
		if self.isEmpty==True:
			print("Stack Empty")
			return
		return self.stack[-1]

stack=Stack()
print("0.Exit")
print("1.Push")
print("2.Pop")
print("3.Peek")

while True:
	x=int(input("Enter Choice:"))
	if x==0:
		break
	elif x==1:
		stack.push(input())
	elif x==2:
		print("Popped ",stack.pop())
	elif x==3:
		print("Peeked ",stack.peek())
	else:
		print("0.Exit")
		print("1.Push")
		print("2.Pop")
		print("3.Peek")

print("Gracefully exited")