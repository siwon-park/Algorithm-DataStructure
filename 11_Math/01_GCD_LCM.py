# 유클리드 호제법

# 최대 공약수(Great Common Divisor)
def gcd(a, b):
    while b > 0:
        a, b = b, a % b # a를 b로 나눈 나머지와 b의 최대 공약수 == a와 b의 최대 공약수
    return a

# 최소 공배수(Least Common Multiple)
def lcm(a, b):
    return a * b / gcd(a, b)
