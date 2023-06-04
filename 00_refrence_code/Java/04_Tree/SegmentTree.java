// 세그먼트 트리 (구간의 합을 구하는 세그먼트 트리)
class SegmentTree {
    int[] arr;
    int[] tree;

    SegmentTree(int n, int[] arr) {
        this.tree = new int[n * 4];
        this.arr = arr;
    }

    int init(int s, int e, int n) {
        if (s == e) return tree[n] = arr[s];
        int mid = (s + e) / 2;
        return tree[n] = init(s, mid, n * 2) + init(mid + 1, e, n * 2 + 1);
    }

    // 업데이트 연산1 -> 업데이트 연산2와 동일함
    int update(int s, int e, int n, int idx, int val) {
        if (idx < s || e < idx) return tree[n];
        if (idx == s && e == idx) return tree[n] = val;
        int mid = (s + e) / 2;
        return tree[n] = update(s, mid, n * 2, idx, val) + update(mid + 1, e, n * 2 + 1, idx, val);
    }

    // 업데이트 연산2 -> 업데이트 연산1과 동일함
    void update2(int s, int e, int n, int idx, int val) {
        if (idx < s || e < idx) return;
        tree[n] += val; // idx를 포함하는 모든 구간에 대해서 val값을 업데이트 하므로 업데이트 연산1과 결국 같음
        if (s == e) return;
        int mid = (s + e) / 2;
        update2(s, mid, n * 2, idx, val);
        update2(mid + 1, e, n * 2 + 1, idx, val);
    }

    int sum(int s, int e, int n, int l, int r) {
        if (r < s || e < l) return 0;
        if (l <= s && e <= r) return tree[n];
        int mid = (s + e) / 2;
        return sum(s, mid, n * 2, l, r) + sum(mid + 1, e, n * 2 + 1, l, r);
    }

}
