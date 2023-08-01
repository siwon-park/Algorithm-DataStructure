class PersistentSegmentTree {
	
	Node[] root; // 루트
	int[] arr; // 초기 배열
	
	PersistentSegmentTree(int[] arr) {
		this.root = new Node[100_555]; // 쿼리의 수만큼 넉넉하게 크기를 설정
		for (int i = 0; i < 100_555; i++) root[i] = new Node();
		this.arr = arr;
	}
	
	void init(Node node, int s, int e) { // 0번 세그먼트 트리 생성
		if (s == e) {
			node.val = arr[s];
			return;
		}
		int mid = (s + e) / 2;
		node.left = new Node();
		node.right = new Node();
		init(node.left, s, mid);
		init(node.right, mid + 1 , e);
		node.val = node.left.val + node.right.val;
		return;
	}
	
	void update(Node prev, Node now, int s, int e, int idx, int v) { // prev는 과거 세그먼트 트리 루트
		if (s == e) {
			now.val = v;
			return;
		}
		int mid = (s + e) / 2;
		if (idx <= mid) { // 왼쪽 자식 노드를 업데이트 하는 경우
			now.left = new Node(); // 왼쪽에 새로운 자식 노드 생성
			now.right = prev.right; // 오른쪽 자식 노드는 재활용
			update(prev.left, now.left, s, mid, idx, v);
		} else { // 오른쪽 자식 노드를 업데이트 하는 경우
			now.right = new Node(); // 오른쪽에 새로운 자식 노드 생성
			now.left = prev.left; // 왼쪽 자식 노드는 재활용
			update(prev.right, now.right, mid + 1, e, idx, v);
		}
		now.val = now.left.val + now.right.val;
		return;
	}
	
	long query(Node node, int s, int e, int l, int r) { // 구간 [l, r]의 값 반환
		if (r < s || e < l) return 0;
		if (l <= s && e <= r) return node.val;
		int mid = (s + e) / 2;
		return query(node.left, s, mid, l, r) + query(node.right, mid + 1, e, l, r);
	}
	
}


class Node {
	long val; // 노드의 값
	Node left, right; // 왼쪽, 오른쪽 노드
	
	Node() {
		this.val = 0;
	}
}