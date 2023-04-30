# 행렬 90도 회전
def rotate_90(arr):
    N = len(arr) # 행 길이
    M = len(arr[0]) # 열 길이
    res = [[0]*N for i in range(M)] # 90도 회전이니 행과 열의 길이가 서로 바뀐다
    for r in range(N):
        for c in range(M):
            res[c][r] = arr[N-r-1][c]
            #res[c][N-r-1] = arr[r][c]
    return res

# 행렬 180도 회전
def rotate_180(arr):
    N = len(arr)  # 행 길이
    M = len(arr[0]) # 열 길이
    res = [[0]*M for i in range(N)] # 180도 회전이니 행과 열은 그대로이다
    for r in range(N):
        for c in range(M):
            res[r][c] = arr[N-1-r][M-1-c]
            #res[N-1-r][M-1-c] = arr[r][c]
    return res

# 행렬 270도 회전
def rotate_270(arr):
    N = len(arr) # 행 길이
    M = len(arr[0])  # 열 길이
    res = [[0]*N for i in range(M)] # 270도 회전이니 행과 열의 길이가 서로 바뀐다
    for r in range(N):
        for c in range(M):
            res[c][r] = arr[r][M-1-c]
            #res[M-1-c][r] = arr[r][c]
    return res

arr2 = [
    [1, 2],
    [3, 4],
    [5, 6]
]

ret1 = rotate_90(arr2)
for lst in ret1:
    print(lst)
print("=====================")

ret2 = rotate_180(arr2)
for lst in ret2:
    print(lst)
print("=====================")

ret3 = rotate_270(arr2)
for lst in ret3:
    print(lst)
print("=====================")
