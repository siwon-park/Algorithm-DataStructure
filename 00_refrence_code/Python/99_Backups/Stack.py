# 직접 스택 구현(연결 리스트 활용)

# 연결리스트를 구현할 노드 클래스 선언
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

# 스택 클래스 선언
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, item):
        self.top = Node(item, self.top) # self.top.next에 self.top(=None을 넣음), self.top.next = None임
        self.size += 1

    def pop(self): # pop은 스택의 마지막 요소를 뽑은 다음 반환
        if self.size == 0: # 스택이 비어있으면 pop을 할 수 없음
            return
        item = self.top.item # item 변수에 스택의 마지막 요소의 값인 self.top.item을 할당하고
        self.top = self.top.next # 스택의 마지막 요소를 self.top.next(=None)으로 바꾼다(=요소를 뽑아서 없앰)
        self.size -= 1
        return item

    def isEmpty(self):
        return self.top is None

    def peek(self): # peek은 스택의 마지막 요소를 뽑지는 않고 반환만 함
        return self.top.item

stack = Stack()
stack.push(4)
stack.push(5)
print(stack.peek()) # 5 (요소를 뽑지는 않음)
print(stack.size) # 2
print(stack.isEmpty()) # False
print(stack.pop()) # 5
print(stack.pop()) # 4
print(stack.isEmpty()) # True
