# 분할정복으로 최솟값(인덱스) 찾기
arr = [55, 78, 12, 20, 45, 7, 42]

def find_min(s, e):
    print(s,e,"======")
    if s == e:
        return s
    else:
        mid = (s + e) // 2
        l = find_min(s, mid)
        r = find_min(mid + 1, e)
        print("l:", l, "r:", r)
        return l if arr[l] < arr[r] else r

print(find_min(0, len(arr) - 1))
