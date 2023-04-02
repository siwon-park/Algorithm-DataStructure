# 최소 힙 구현
# 최소 힙은 이진 트리 상 루트에 가장 작은 값이 있어야함
last = 0

def push(item):
    global last
    # full check
    last += 1
    tree[last] = item
    c = last
    p = last//2
    while p and tree[p] > tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2

def pop():
    global last
    # empty check(last == 0)
    root = tree[1]
    tree[1] = tree[last]
    last -= 1
    p = 1
    c = 2
    while c <= last:
        if c+1 <= last and tree[c] > tree[c+1]:
            c += 1
        if tree[p] > tree[c]:
            tree[p], tree[c] = tree[c], tree[p]
            p = c
            c = p*2
        else:
            break

    return root

data = [4, 2, 5, 23, 10, 1, 19, 8, 7, 11, 3]
N = len(data) # 11

# push 테스트
tree = [0] * (N+1)
for val in data:
    push(val)
# print(tree) # [0, 1, 3, 2, 7, 4, 5, 19, 23, 8, 11, 10]

# pop 테스트
n = 0
while n < N:
    print(pop())
    n += 1
