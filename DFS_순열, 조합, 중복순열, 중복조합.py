#DFS로 순열, 조합, 중복순열, 중복조합 구현하기
#1 순열
result=[]
def permute(elements,arr):
    if not elements:
        result.append(arr[:])
        return
    for i in elements:
        left_elements=elements[:]
        left_elements.remove(i)
        permute(left_elements,arr+[i])
permute([1,2,3],[])
print(result) #[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

#2 조합
result=[]
elements=[2,4,5,8]
n=len(elements)
def combine(start,k,arr):
    if k==0:
        result.append(arr[:])
        return
    for i in range(start,n):
        combine(i+1,k-1,arr+[elements[i]])
combine(0,3,[])
print(result) #[[2, 4, 5], [2, 4, 8], [2, 5, 8], [4, 5, 8]]

#3 중복순열
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
#[3, 2, 3], [3, 3, 1], [3, 3, 2], [3, 3, 3]] #27개

#4 중복 조합
result=[]
elements=[2,4,9]
n=len(elements)
def combine_with_replacement(start,k,arr):
    if k==0:
        result.append(arr[:])
        return
    for i in range(start,n):
        combine_with_replacement(i,k-1,arr+[elements[i]])
combine_with_replacement(0,2,[])
print(result) #[[2, 2], [2, 4], [2, 9], [4, 4], [4, 9], [9, 9]]
