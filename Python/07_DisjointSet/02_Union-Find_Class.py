# 클래스로 구현한 유니온-파인드(disjointset)
class DisjointSet:
    def __init__(self, n):
        self.group = list(range(n+1)) # 그룹(parent 배열)
        self.size = [1] * (n+1) # 해당 그룹의 크기

    def find(self, u):
        if u == self.group[u]:
            return u
        self.group[u] = self.find(self.group[u])
        return self.group[u]

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u != v:
            self.group[u] = v
            self.size[v] += self.size[u]