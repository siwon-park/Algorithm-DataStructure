# KMP(Knuth–Morris–Pratt) 알고리즘

# 패턴 P의 길이를 M, 전체 문자열 S의 길이를 N이라고 할 때,
# 어떠한 경우더라도 O(N + M)의 시간 복잡도로 패턴매칭을 찾을 수 있는 알고리즘

# 실패 함수(불일치가 발생했을 때, j가 어디로 이동해야 하는지를 반환)
# 패턴에서 반복적으로 등장하는 구간을 찾음
def find_fail(p):
    fail = [0] * M
    j = 0
    for i in range(1, M): # i = 1부터 시작하는 이유는 i = 0일 때, p[i] == p[j]이기 때문
        while j > 0 and p[i] != p[j]:
            j = fail[j - 1] # 불일치가 발생했을 경우 j가 이동해야할 위치를 fail 배열에 기록
        if p[i] == p[j]:
            j += 1
            fail[i] = j
    # print(fail)
    return fail

# KMP
def kmp(t, p):
    ret = []
    fail = find_fail(p)
    j = 0
    for i in range(N):
        while j > 0 and t[i] != p[j]:
            j = fail[j - 1]
        if t[i] == p[j]:
            if j == M - 1: # t[i]와 p[i]가 일치하면서 j가 0에서 출발해서 M - 1까지 왔다면, 길이 M 동안 일치했다는 의미이므로 패턴이 매칭됨
                ret.append(i - M + 1) # M - 1만큼 왔으니까 매칭되는 패턴의 시작 위치는 i - M + 1임
                j = fail[j]
            else:
                j += 1
    return ret

# 예시 1
t = "abc abcdab abcdabcdabde"
p = "abcdabd"

N = len(t)
M = len(p)

print(kmp(t, p))

# 예시 2
t = "abcdeabcfabcdabc"
p = "abcdabc" # fail = [0, 0, 0, 0, 1, 2, 3]

N = len(t)
M = len(p)

print(kmp(t, p))