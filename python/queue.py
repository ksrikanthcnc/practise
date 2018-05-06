class Queue:
	def __init__(self):
		self.queue=[]
	def isEmpty(self):
		return self.queue==[]
	def enqueue(self,data):
		self.queue.append(data)
	def dequeue(self):
		if queue.isEmpty()==True:
			print("Queue Empty")
			return
		data=self.queue[0]
		del self.queue[0]
		return data
	def peek(self):
		if queue.isEmpty()==True:
			print("Queue Empty")
			return
		return self.queue[0]

queue=Queue()
print("0.Exit")
print("1.Enqueue")
print("2.Dequeue")
print("3.Peek")

while True:
	x=int(input("Enter Choice:"))
	if x==0:
		break
	elif x==1:
		queue.enqueue(input())
	elif x==2:
		print("Dequeue ",queue.dequeue())
	elif x==3:
		print("Peeked ",queue.peek())
	else:
		print("0.Exit")
		print("1.Enqueue")
		print("2.Dequeue")
		print("3.Peek")

print("Gracefully exited")