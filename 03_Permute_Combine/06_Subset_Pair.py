# 부분 집합 쌍 구하기

# 1) 비트 연산으로 부분 집합 구하기
N = 4
# 중복을 없애려면 N-1번 비트 연산을 하는 이유는 N개 했을 때 a개 나온다면
# 중복을 제거한다 했을 때 a/2개 이므로 N-1번 비트 연산하면 1/2가 되니까 그렇다.
for subset in range(1 << (N - 1)):
    A, B = [], []
    for i in range(N):
        if subset & (1 << i):
            A.append(i)
        else:
            B.append(i)
    if len(A) == len(B):
        print(A, B)


# 2) 재귀함수로 부분집합 구하기
N = 4
# A, B 둘 다 빈 리스트이고 subset(0)를 하면 중복이 발생함
A = [0] # 중복을 제거하려면 A에 [0]을 넣고 시작
B = []

def subset(k):
    if k == N:
        if len(A) == len(B):
            print(A, B)
        return
    else:
        # k를 A에 포함시키는 경우
        A.append(k)
        subset(k+1)
        A.pop()
        # k를 B에 포함시키는 경우
        B.append(k)
        subset(k+1)
        B.pop()

subset(1) # A에 0을 넣고 시작했으므로, subset을 만들 때 1부터 넣게 1부터 출발시킴
