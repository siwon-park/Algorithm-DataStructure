# 유클리드 호제법

# 최대 공약수(Great Common Divisor)
def gcd(a, b):
    while b > 0:
        a, b = b, a % b # a를 b로 나눈 나머지와 b의 최대 공약수 == a와 b의 최대 공약수
    return a


# 곱셈의 역원(코드 이해가 안 가지만 일단 기록)
def gcd_ext(a, b):
    q, r = a, b
    x, y = 1, 0
    while r:
        x, y = y, x - (q//r)*y
        q, r = r, q % r
    y = (q - a*x) // b
    return q, x, y


# 최소 공배수(Least Common Multiple)
def lcm(a, b):
    return a * b / gcd(a, b)


# 카잉 달력 문제 예시
t = int(input())
for _ in range(t):
    m, n, x, y = [int(x) for x in input().split()]
    g, a, b = gcd_ext(m, n)
    if x % g != y % g:
        print(f'-1\n')
        continue
    r = ((m * a * y + n * b * x) // g) % lcm(m, n)
    print(f'{r if r != 0 else lcm(m, n)}\n')