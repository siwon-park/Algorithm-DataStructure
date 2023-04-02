tree = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # tree = [0] * (N+1)
N = 10 # N은 노드의 수

def preorder(v):
    if v > N:
        return
    print(tree[v], end=" ")
    preorder(2*v)
    preorder(2*v+1)

def inorder(v):
    if v > N:
        return
    inorder(2*v)
    print(tree[v], end=" ")
    inorder(2*v+1)

def postorder(v):
    if v > N:
        return
    postorder(2*v)
    postorder(2*v+1)
    print(tree[v], end=" ")

preorder(1) # 1 2 4 8 9 5 10 3 6 7
inorder(1) # 8 4 9 2 10 5 1 6 3 7
postorder(1) # 8 9 4 10 5 2 6 7 3 1
