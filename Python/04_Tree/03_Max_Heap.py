# 최대 힙(Max_Heap)
last = 0

# 힙 푸시
def push(item):
    global last
    if last == N: # last == N이면 Full
        return

    last += 1 # last의 초깃값은 0이므로 1 증가시킨 뒤 루트(1)에 삽입
    tree[last] = item
    c = last
    p = c // 2
    while p and tree[p] < tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c // 2

# 힙 팝
def pop():
    global last
    if last == 0: # last == 0이면 empty
        return
    
    max_value = tree[1]
    tree[1] = tree[last]
    last -= 1
    p = 1
    c = 2
    while c <= last:
        # 오른쪽 자식이 있는지 체크하면서 오른쪽 자식의 값을 체크
        if c+1 <= last and tree[c] < tree[c+1]:
            c += 1
        if tree[p] < tree[c]:
            tree[p], tree[c] = tree[c], tree[p]
            p = c  # 부모 인덱스를 자식 인덱스로 변경하고
            c = p*2  # 자식 인덱스를 바뀐 부모 인덱스*2 해준다
        else:
            break
    
    return max_value

data = [4, 2, 5, 23, 10, 1, 19, 8, 7, 11, 3]
N = len(data)
tree = [0] * (N+1)

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
