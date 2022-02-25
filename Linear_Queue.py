# 선형 큐 구현
class LinearQueue:
    def __init__(self, max_size):
        self.q = [0] * max_size
        self.size = max_size
        self.front = -1
        self.rear = -1

    def isFull(self):
        return self.rear == self.size - 1

    def isEmpty(self):
        return self.rear == self.front

    def enQueue(self, item):
        if LinearQueue.isFull(self):
            print("Can't Append Item Because Of Queue OverFlow")
            return
        self.rear = self.rear + 1
        self.q[self.rear] = item

    def deQueue(self):
        if LinearQueue.isEmpty(self):
            print("Can't Pop From Empty Queue")
            return
        self.front = self.front + 1
        return self.q[self.front]

q = LinearQueue(4)
for i in range(4):
    q.enQueue(i+1)
print(q.q, q.front, q.rear)
while not q.isEmpty():
    print(q.deQueue())