# 최소 힙(Min_Heap)
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
    while p and tree[p] > tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c // 2

# 힙 팝
def pop():
    global last
    if last == 0: # last == 0이면 empty
        return

    min_value = tree[1] # 팝하여 리턴할 값에 루트의 값을 할당하고
    tree[1] = tree[last] # 루트의 자리에 last의 원소의 값을 넣음
    last -= 1 # last는 루트로 이동했으니 -1을 해줌
    p = 1
    c = 2
    while c <= last:
        # 오른족 자식이 있는지 체크하면서 오른쪽 자식의 값을 확인
        if c+1 <= last and tree[c] > tree[c+1]:
            c += 1
        if tree[p] > tree[c]:
            tree[p], tree[c] = tree[c], tree[p]
            p = c # 부모 인덱스를 자식 인덱스로 변경하고
            c = p*2 # 자식 인덱스를 바뀐 부모 인덱스*2 해준다
        else: # 부모의 값이 자식보다 작다면 밑에 다른 자식들도 부모보다 큰 값이므로 탐색 종료
            break

    return min_value

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
    