# 계수 정렬
# 방법 1) enumerate활용
def counting_sort1(arr):
    M = max(arr)
    ret = []
    count = [0] * (M+1)
    for n in arr:
        count[n] += 1

    for i, v in enumerate(count):
        ret.extend([i] * v)

    return ret

# 방법2) 카운팅 배열 누적합 활용
def counting_sort2(arr):
    N = len(arr)
    M = max(arr)
    ret = [0] * N
    count = [0] * (M+1)
    for n in arr:
        count[n] += 1

    for i in range(1, M+1):
        count[i] += count[i-1]
    
    for i in range(N-1, -1, -1):
        count[arr[i]] -= 1
        ret[count[arr[i]]] = arr[i]

    return ret

# 방법 3) 2중 for 구문 활용
def counting_sort3(arr):
    M = max(arr)
    ret = []
    count = [0] * (M+1)
    for n in arr:
        count[n] += 1
    
    for i in range(M+1):
        for j in range(count[i]):
            ret.append(i)
            
    return ret

arr = [10, 2, 3, 5, 2, 11, 12, 11, 10, 15, 10, 4, 6]
ret = counting_sort1(arr)
print(ret)

ret2 = counting_sort2(arr)
print(ret2)

ret3 = counting_sort3(arr)
print(ret3)