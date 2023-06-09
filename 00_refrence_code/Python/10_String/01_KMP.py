# KMP(Knuth–Morris–Pratt)

# 실패 함수 -> 불일치가 발생했을 때, 어느 위치로 이동해야 하는지를 반환 (일치하는 접두/접미사의 최대 길이)
def find_fail(w: str) -> list:
    fail = [0] * M
    j = 0 # w의 인덱스
    for i in range(1, M): # i = 1부터 시작하는 이유는 i = 0일 때, p[i] == p[j]이기 때문
        while j > 0 and w[i] != w[j]:
            j = fail[j - 1] # 불일치 발생 시 fail 배열에 기록된 숫자만큼 건너뜀
        if w[i] == w[j]:
            # 불일치가 발생했을 경우 이동해야 할 위치를 fail 배열에 기록 (j번 째까진 일치했으니 실패 시 j + 1인 곳으로 이동)
            j += 1
            fail[i] = j
    # print(fail)
    return fail


# KMP
def kmp(s: str, w: str) -> list:
    ret = []
    fail = find_fail(w)
    j = 0 # w의 인덱스
    for i in range(N): # i는 s의 인덱스
        while j > 0 and s[i] != w[j]:
            j = fail[j - 1]
        if s[i] == w[j]: # 일치할 경우 (1)
            if j == M - 1: # j가 0에서 출발해서 M - 1까지 왔다면, 길이 M 동안 일치했다는 의미이므로 패턴이 매칭됨 (3)
                ret.append(i - M + 1) # M - 1만큼 왔으니까 매칭되는 패턴의 시작 위치는 i - M + 1임
                j = fail[j]
            else: # j가 M - 1이 아니면 아직 M만큼 오지 않았으므로 j를 증가 (2)
                j += 1
    return ret


# 예시 1
t1 = "abc abcdab abcdabcdabde"
p1 = "abcdabd"

N = len(t1)
M = len(p1)

print(kmp(t1, p1)) # [15]

# 예시 2
t2 = "abcdeabcfabcdabc"
p2 = "abcdabc" # fail = [0, 0, 0, 0, 1, 2, 3]

N = len(t2)
M = len(p2)

print(kmp(t2, p2)) # [9]