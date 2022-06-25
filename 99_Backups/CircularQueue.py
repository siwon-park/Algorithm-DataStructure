# 원형 큐 구현
class CircularQueue:
    def __init__(self, max_size):
        self.q = [0] * max_size # [None] * max_size # 삽입되는 요소가 0일 수도 있으니 None으로 초기화
        self.size = max_size
        self.front = 0
        self.rear = 0

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def isEmpty(self):
        return self.rear == self.front

    def enQueue(self, item):
        if CircularQueue.isFull(self):
            print("Can't Append Item Because Of Queue OverFlow")
            return
        self.q[self.rear] = item # rear의 default가 0부터 출발했으니 요소 삽입부터 먼저한다
        self.rear = (self.rear + 1) % self.size # rear의 포인터를 옮긴다

    def deQueue(self):
        if CircularQueue.isEmpty(self):
            print("Can't Pop From Empty Queue")
            return
        ret_val = self.q[self.front] # front의 default가 0이니, 반환값을 먼저 기록해준다
        # self.q[self.front] = None # (pop한 요소를 삭제)
        self.front = (self.front + 1) % self.size # front의 포인터를 옮긴다
        return ret_val

cq = CircularQueue(5)

for i in range(1, 5):
    cq.enQueue(i)
while not cq.isEmpty():
    print(cq.deQueue())
    print(cq.front, cq.rear)

# print("front:", cq.front, "rear:", cq.rear)
#
# cq.enQueue(1)
# print("front:", cq.front, "rear:", cq.rear)
# cq.enQueue(2)
# print("front:", cq.front, "rear:", cq.rear)
# cq.enQueue(3)
# print("front:", cq.front, "rear:", cq.rear)
# cq.enQueue(4)
# print("front:", cq.front, "rear:", cq.rear)
#
# print(cq.deQueue())
# print("front:", cq.front, "rear:",cq.rear)
# print(cq.deQueue())
# print("front:", cq.front, "rear:",cq.rear)
#
# cq.enQueue(5)
# print("front:", cq.front, "rear:",cq.rear)
# cq.enQueue(6)
# print("front:", cq.front, "rear:",cq.rear)