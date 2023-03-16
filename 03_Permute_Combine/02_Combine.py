# 조합
arr = [1, 2, 3]
N = len(arr)

# N개 중 k개를 뽑는 조합
ret = []


def combine(k, s, lst):
    if k == 0:
        ret.append(lst)
        return
    for i in range(s, N):
        combine(k - 1, i + 1, lst + [arr[i]])

combine(2, 0, [])
print(ret) # [[1, 2], [1, 3], [2, 3]]