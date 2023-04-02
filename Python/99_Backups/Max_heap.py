# 최대 힙 구현
# 최대 힙은 이진 트리상 루트에 가장 큰 값이 있어야함
last = 0

def push(item):
    global last
    # full 체크(last == N이면 full인 상태이므로 넣으면 안 됨)
    last += 1 # last에 +1을 하여 last를 인덱스로 사용해서 tree배열에 item 삽입
    tree[last] = item
    c = last # c는 자식의 인덱스
    p = last//2 # p는 부모의 인덱스 (루트의 인덱스는 1이고, 여기서 //2를 하면 0임)
    while p and tree[p] < tree[c]: # p가 0이 아니고, 자식이 부모보다 큰 동안 반복
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2

def pop():
    global last
    # empty 체크(last == 0이면 empty)
    root = tree[1] # root 변수에 루트 노드의 값을 저장함
    tree[1] = tree[last] # 루트 노드에 마지막 노의 값을 저장함(옮길 예정)
    last -= 1 # last는 이제 빈 상태이니 -1을 해줌(실제로 빈 상태는 아님, 어차피 push하면서 덮어씌워지기 때문에 큰 상관없음)
    p = 1
    c = 2
    while c <= last:
        if c+1 <= last and tree[c] < tree[c+1]: # 오른쪽 자식이 있으면 왼쪽 자식은 항상 있지만, 왼쪽 자식이 있을 때, 오른쪽 자식이 있는지는 확인해야봐야하는 사항임
            c += 1
        if tree[p] < tree[c]:
            tree[p], tree[c] = tree[c], tree[p]
            p = c
            c = 2*p
        else:
            break

    return root # 맨처음 저장해뒀던 루트값을 반환

data = [4, 2, 5, 23, 10, 1, 19, 8, 7, 11, 3]
N = len(data) # 11

# push 테스트
tree = [0] * (N+1)
for val in data:
    push(val)
# print(tree) # [0, 23, 11, 19, 8, 10, 1, 4, 2, 7, 5, 3] 배열 상으론 이렇게 들어가 있지만, 이진힙으로 구성되어 있음

# pop 테스트
n = 0
while n < N:
    print(pop())
    n += 1
