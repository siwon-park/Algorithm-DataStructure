#DFS로 순열, 조합, 중복순열, 중복조합 구현하기
#############################################
# 1 순열(DFS)
# 중복을 피하기 위해 새로운 배열을 copy하고 copy한 배열에서 넣은 요소를 제거해준 뒤 DFS
result=[]
def permute(elements,arr):
    if not elements:
        result.append(arr[:])
        return
    for i in elements:
        left_elements=elements[:] #기존 배열을 복사
        left_elements.remove(i) #복사한 새 배열에서 i를 제거
        permute(left_elements,arr+[i])
permute([1,2,3],[])
print(result) #[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

# 1-1 순열1 (백트랙킹, 자리 바꾸기 개념활용)
ret = []
def permute1(i, N):
    if i == N:
        ret.append(p[:])
        return
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            permute(i+1, N)
            p[i], p[j] = p[j], p[i]

p = [1, 2, 3]
permute(0, 3)
print(ret)

# 1-2 순열2 (백트랙킹)
def permute2(k, N):
    if k == N:
        print(*order)
    else:
        for first in arr:
            if first in order:
                continue
            order.append(first)
            permute2(k+1, N)
            order.pop()
            
arr = [1, 2, 3]
order = []
permute2(0, 3)

# 2 조합
# 이미 뽑은 요소를 또 뽑지 않기 위해 뽑은 요소의 인덱스+1을 하여 중복을 피해준다
result=[]
elements=[2,4,5,8]
n=len(elements)
def combine(start,k,arr):
    if k==0:
        result.append(arr[:])
        return
    for i in range(start,n):
        combine(i+1,k-1,arr+[elements[i]]) #i+1을 하여 이미 뽑은 요소를 못 뽑아 중복을 피함
combine(0,3,[])
print(result) #[[2, 4, 5], [2, 4, 8], [2, 5, 8], [4, 5, 8]]

# 3 중복순열
# 중복을 허락하므로, 요소를 계속 추가하다가 길이가 n이되면 반환한다
result=[]
elements=[1,2,3]
n=len(elements)
def products(arr,n):
    if n==0:
        result.append(arr[:])
        return
    for i in elements:
        products(arr+[i],n-1)
products([],3)
print(result) #[[1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2, 1], [1, 2, 2], [1, 2, 3], [1, 3, 1],
#[1, 3, 2], [1, 3, 3], [2, 1, 1], [2, 1, 2], [2, 1, 3], [2, 2, 1], [2, 2, 2], [2, 2, 3],
#[2, 3, 1], [2, 3, 2], [2, 3, 3], [3, 1, 1], [3, 1, 2], [3, 1, 3], [3, 2, 1], [3, 2, 2],
#[3, 2, 3], [3, 3, 1], [3, 3, 2], [3, 3, 3]] #27개(3^3개)

# 4 중복 조합
# 중복을 허락하므로 뽑은 요소의 인덱스를 그대로 둔다
# 단, 순서가 다른 것은 허락하지 않으므로, for i in range(start,n)으로 range(범위) 탐색을 해야한다.
# 왜냐하면 for i in elements로 요소에 대해 (중복)탐색을 해버리면, 아래 예시에서 처음에 2를 뽑고 9를 뽑아 [2,9]가 나오고, 처음에 9를 뽑고 그다음 2를 뽑아 [9,2]도 나오기 때문임
# 즉, 처음에 만약 9를 뽑았다면 그다음에 또 9를 뽑고 끝내야 하지 2를 탐색하지 못하게 해야함. 따라서 for i in range(start,n)과 같이 인덱스로 dfs탐색을 해주는 것임
result=[]
elements=[2,4,9]
n=len(elements)
def combine_with_replacement(start,k,arr):
    if k==0:
        result.append(arr[:])
        return
    for i in range(start,n):
        combine_with_replacement(i,k-1,arr+[elements[i]]) #중복은 허락하되, 순서가 다른 것은 허락하지 않으므로 이미 뽑았던 요소의 인덱스 i에서 출발
combine_with_replacement(0,2,[])
print(result) #[[2, 2], [2, 4], [2, 9], [4, 4], [4, 9], [9, 9]]
