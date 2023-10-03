/*
* 펜윅 트리 (구간 합 연산 및 갱신)
* 백준 구간 합 구하기 (2042번) 소스 코드 참조: https://www.acmicpc.net/source/63472849
*/
class FenwickTree {
	
	long[] tree;
	int treeSize;
	
	FenwickTree(int n) {
		// 1부터 n 포함이기 때문에 n + 1
		this.tree = new long[n + 1];
		this.treeSize = n + 1;
	}
	
	// 업데이트할 값과 현재 값의 차이인 v만큼을 대상 구간에 갱신시켜주고, 배열의 해당 위치 값을 업데이트한 결과값으로 변경
	void update(int i, long v) {
		while (i < treeSize) { // treeSize가 n + 1이기 때문에 n까지 계산하기 위해 n + 1보다 작을 동안 반복
			tree[i] += v;
			i += (i & -i);
		}
	}
	
	// 구간 [a, b]의 합은 구간 [1, b]에서 구간 [1, a-1]을 뺀 것과 같다
	long sum(int i) {
		long ans = 0;
		while (i > 0) {
			ans += tree[i];
			i -= (i & -i);
		}
		return ans;
	}
}