// 구간 합을 연산하는 Lazy Propagation
class LazyPropagation {

    int[] arr;
    int[] tree;
    int[] lazy; // lazy 배열

    LazyPropagation(int N, int[] arr) {
        this.tree = new int[N * 4];
        this.lazy = new int[N * 4];
        this.arr = arr;
    }

    void lazyPropagation(int s, int e, int n) {
        // 처리해야할 일이 남아 있다면
        if (lazy[n] != 0) {
            // 관리하는 구간의 개수만큼 미리 계산해서 결과를 변경시켜줌
            tree[n] += (e - s + 1) * lazy[n];
            // 만약 현재 구간이 리프 노드가 아니라면
            if (s != e) {
                // 자식들에게 lazy를 전파함
                lazy[n * 2] += lazy[n];
                lazy[n * 2 + 1] += lazy[n];
            }
            // 현재 구간의 lazy 값을 0으로 만듦
            lazy[n] = 0;
        }
    }

    // 세그먼트 트리의 초기화 함수
    void init(int s, int e, int n) {
        if (s == e) {
            tree[n] = arr[s];
            return;
        }
        int mid = (s + e) / 2;
        init(s, mid, n * 2);
        init(mid + 1, e, n * 2 + 1);
        tree[n] = tree[n * 2] + tree[n * 2 + 1];
    }

    // 특정 인덱스의 값을 변경하는 것이 아니라 특정 구간의 값들을 변경
    int update(int s, int e, int n, int l, int r, int val) {
        // 노드를 확인하기 전에 lazy 배열을 확인하여 전파할 값이 있다면 전파함
        lazyPropagation(s, e, n);
        if (r < s || e < l) return tree[n];
        if (l <= s && e <= r) {
            // lazy 배열에 값을 추가하여 현재 구간에서 해결해야 할 일을 추가함
            lazy[n] += val;
            // 전파
            lazyPropagation(s, e, n);
            // 현재 구간에서는 값 변경이 적용되었고, 자식 노드로 전파가 완료되었으므로 return하면 됨
            // 자식의 값은 해당 자식이 참조될 때 lazy의 값을 확인하고 업데이트 될 예정
            // 단, 만약 자식이 참조되지 않는다면 영원히 업데이트 되지 않음
            return tree[n];
        }
        int mid = (s + e) / 2;
        tree[n] = update(s, mid, n * 2, l, r, val) + update(mid + 1, e, n * 2 + 1, l, r, val);
        return tree[n];
    }

    // 구간의 합을 반환
    int sum(int s, int e, int n, int l, int r) {
        // 전파할 일이 남아있다면, 전파한 다음에 처리
        lazyPropagation(s, e, n);
        if (r < s || e < l) return 0;
        if (l <= s && e <= r) return tree[n];
        int mid = (s + e) / 2;
        return sum(s, mid, n * 2, l, r) + sum(mid + 1, e, n * 2 + 1, l, r);
    }
}
