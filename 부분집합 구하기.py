# 부분집합 구하기
arr = [3, 1, 2, 4]
N = len(arr)

# 1) 재귀함수 활용
ret = []

def combine(arr, s, lst, N):
    ret.append(lst[:])
    for i in range(s, N):
        combine(arr, i+1, lst+[arr[i]], N)

combine(arr, 0, [], len(arr))

ret.sort()
print(ret, len(ret)) # [[], [1], [1, 2], [1, 2, 4], [1, 4], [2], [2, 4], [3], [3, 1], [3, 1, 2], [3, 1, 2, 4], [3, 1, 4], [3, 2], [3, 2, 4], [3, 4], [4]] 16

# 2) 비트연산 활용
ret2 = []

for i in range(1<<N):
    lst = []
    for j in range(N):
        if i & (1<<j):
            lst.append(arr[j])
    ret2.append(lst)

ret2.sort()
print(ret2, len(ret2)) # [[], [1], [1, 2], [1, 2, 4], [1, 4], [2], [2, 4], [3], [3, 1], [3, 1, 2], [3, 1, 2, 4], [3, 1, 4], [3, 2], [3, 2, 4], [3, 4], [4]] 16

# 비트 연산 활용 예시)
arr = 'ABCD'
N = len(arr)
for subset in range(1 << N): # 중복을 방지하려면 (1 << (N - 1))
    cnt = 0
    A, B = [], []
    for i in range(N):
        if subset & (1 << i):
            A.append(arr[i])
        else:
            B.append(arr[i])

    if len(A) == len(B):
        print(A, B)
