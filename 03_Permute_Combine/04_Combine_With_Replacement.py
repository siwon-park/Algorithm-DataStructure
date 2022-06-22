# 중복 조합(combine with replacement) # n H r = n+r-1 C r
arr = [1, 2, 3]
N = len(arr)

# N개의 요소 중 k개를 중복으로 뽑음
ret = []

def comb_w_replace(k, s, lst):
    if k == 0:
        ret.append(lst)
        return
    for i in range(s, N):
        comb_w_replace(k-1, i, lst+[arr[i]])

comb_w_replace(2, 0, [])
print(ret)