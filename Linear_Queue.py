# 선형 큐 구현
class LinearQueue:
    def __init__(self, max_size):
        self.q = [0] * max_size # [None] * max_size # 삽입되는 요소가 0일 수도 있으니 None으로 초기화
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
        self.rear = self.rear + 1 # rear의 default가 -1이니 1증가시킨 다음 삽입을 시작함
        self.q[self.rear] = item

    def deQueue(self):
        if LinearQueue.isEmpty(self):
            print("Can't Pop From Empty Queue")
            return
        self.front = self.front + 1 # front의 default가 -1이니 1증가시킨 다음 삭제
        return self.q[self.front]

q = LinearQueue(4)
for i in range(4):
    q.enQueue(i+1)
print(q.q, q.front, q.rear)
while not q.isEmpty():
    print(q.deQueue())
