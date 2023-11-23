class CircularQueue:
    def __init__(self, capacity):
        self.front = 1
        self.rear = 0
        self.size = 0
        self.capacity = capacity
        self.queue = [None] * capacity

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def clear(self):
        self.front = self.rear = self.size = 0
        self.queue = [None] * self.capacity

    def enqueue(self, data):
        if self.isFull():
            print("Queue is Full")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        self.queue[self.rear] = data

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        data = self.queue[self.front]
        self.size -= 1
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity

        return data

    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        data = self.queue[self.front]
        return data

    def display(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            index = self.front
            print("Queue :")
            for _ in range(self.size):
                print(self.queue[index], end=" ")
                index = (index + 1) % self.capacity
            print()

cq = CircularQueue(5)
computerData = ["keyboard","mouse","monitor","printer",
                "scanner"]
for data in computerData:
    cq.enqueue(data)

cq.display()
cq.dequeue()
cq.display()
print(cq.peek())
cq.display()
cq.clear()
cq.display()








        


    
