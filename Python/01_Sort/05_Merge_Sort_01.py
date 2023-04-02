# 병합 정렬(배열에 복사하여 결과 반환)
def merge_sort(s, e):
    # 분할/정복
    if s == e:
        return
    mid = (s + e) // 2
    merge_sort(s, mid) # 왼쪽은 mid까지 포함
    merge_sort(mid+1, e) # 오른쪽은 mid+1부터

    i, j, k = s, mid+1, s
    while i <= mid and j <= e:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            i += 1
            k += 1
        else:
            tmp[k] = arr[j]
            j += 1
            k += 1
    while i <= mid:
        tmp[k] = arr[i]
        i += 1
        k += 1
    while j <= e:
        tmp[k] = arr[j]
        j += 1
        k += 1
    
    for i in range(s, e+1):
        arr[i] = tmp[i]

arr = [69, 10, 30, 2, 16, 8, 31, 22, 2]
N = len(arr)
tmp = [0] * N
merge_sort(0, N-1)
print(arr)