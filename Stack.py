# 직접 스택 구현(연결 리스트 활용)

# 연결리스트를 구현할 노드 클래스 선언
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

# 스택 클래스 선언
class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last) # self.last.next에 self.last(=None을 넣음)
        # self.last.next = None임
    def pop(self):
        item = self.last.item
        self.last = self.last.next # None
        return item

    def isEmpty(self):
        return self.last is None

stack = Stack()
stack.push(4)
stack.push(5)
print(stack.isEmpty()) # False
print(stack.pop()) # 5
print(stack.pop()) # 4
print(stack.isEmpty()) # True