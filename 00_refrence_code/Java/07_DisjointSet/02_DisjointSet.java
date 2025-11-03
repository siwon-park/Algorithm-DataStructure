public class DisjointSet {

    private int[] parent;

    public DisjointSet(int n) {
        this.parent = new int[n + 1];
        for (int i = 0; i <= n; i++) parent[i] = i;
    }

    public int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }

    public void union(int a, int b) {
        a = find(a);
        b = find(b);
        // if (a != b) parent[b] = a; // without union by rank; 부모가 다를 경우 조건 없이 b를 a의 부모로 편입
        if (a < b) parent[b] = a;
        else parent[a] = b;
    }

    public boolean isConnected(int a, int b) {
        return find(a) == find(b);
    }
}

