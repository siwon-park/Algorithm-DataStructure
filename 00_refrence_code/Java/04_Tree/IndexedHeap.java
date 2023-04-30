class IndexedHeap <Comp extends PairComparator> {
    int last;
    int maxSize;
    Comp comp;
    int[] memo;
    Pair[] heap;

    IndexedHeap(int n, Comp comp) {
        this.last = 0;
        this.maxSize = n;
        this.comp = comp;
        this.memo = new int[n + 1];
        this.heap = new Pair[n + 1];
    }

    boolean isEmpty() {
        return last == 0;
    }

    boolean isFull() {
        return last == maxSize;
    }

    void add(Pair o) {
        if (isFull()) return;
        heap[++last] = o;
        memo[o.id] = last;

        int c = last;
        int p = c / 2;
        while (p > 0 && comp.compare(heap[c], heap[p])) {
            swap(p, c);
            memo[heap[p].id] = p;
            memo[heap[c].id] = c;
            c = p;
            p = c / 2;
        }
    }

    Pair poll() {
        if (isEmpty()) return null;
        Pair pair = heap[1];
        heap[1] = heap[last--];
        memo[heap[1].id] = 1;

        int p = 1;
        int c = 2 * p;
        while (c <= last) {
            if (c + 1 <= last && comp.compare(heap[c + 1], heap[c])) c += 1;
            if (comp.compare(heap[c], heap[p])) {
                swap(p, c);
                memo[heap[p].id] = p;
                memo[heap[c].id] = c;
                p = c;
                c = 2 * p;
            } else break;
        }

        return pair;
    }

    Pair peek() {
        return heap[1];
    }

    void remove(int id) { // 최소힙이냐 최대힙이냐에 따라 값 변경 기준이 다르므로 위/아래 이동 모두 구현
        int rmIdx = memo[id];
        if (rmIdx > last || rmIdx == 0) return;
        heap[rmIdx] = heap[last--]; // heap[last];
        // heap[last] = new Pair(maxSize, heap[last--].val); // id는 힙 사이즈만큼, 값은 last에 있는 값으로 하여 새 객체 생성
        memo[heap[rmIdx].id] = rmIdx;

        int c = rmIdx;
        int p = c / 2;
        while (p > 0 && comp.compare(heap[c], heap[p])) {
            swap(p, c);
            memo[heap[p].id] = p;
            memo[heap[c].id] = c;
            c = p;
            p = c / 2;
        }

        p = rmIdx;
        c = 2 * p;
        while (c <= last) {
            if (c + 1 <= last && comp.compare(heap[c + 1], heap[c])) c += 1;
            if (comp.compare(heap[c], heap[p])) {
                swap(p, c);
                memo[heap[p].id] = p;
                memo[heap[c].id] = c;
                p = c;
                c = 2 * p;
            } else break;
        }

    }

    void update(int id, int newVal) {
        int upIdx = memo[id];
        if (upIdx > last || upIdx == 0) return;
        heap[upIdx].val = newVal;

        int c = upIdx;
        int p = c / 2;
        while (p > 0 && comp.compare(heap[c], heap[p])) {
            swap(p, c);
            memo[heap[p].id] = p;
            memo[heap[c].id] = c;
            c = p;
            p = c / 2;
        }

        p = upIdx;
        c = 2 * p;
        while (c <= last) {
            if (c + 1 <= last && comp.compare(heap[c + 1], heap[c])) c += 1;
            if (comp.compare(heap[c], heap[p])) {
                swap(p, c);
                memo[heap[p].id] = p;
                memo[heap[c].id] = c;
                p = c;
                c = 2 * p;
            } else break;
        }

    }

    void swap(int p, int c) {
        Pair tmp = heap[c];
        heap[c] = heap[p];
        heap[p] = tmp;
    }

}

class Pair {
    int id;
    int val;

    Pair(int id, int val) {
        this.id = id;
        this.val = val;
    }
}

interface PairComparator {
    boolean compare(Pair o1, Pair o2);
}

class MaxComp implements PairComparator {
    @Override
    public boolean compare(Pair o1, Pair o2) {
        if (o1.val > o2.val) return true;
        else if (o1.val == o2.val && o1.id < o2.id) return true;
        return false;
    }
}

class MinComp implements PairComparator {
    @Override
    public boolean compare(Pair o1, Pair o2) {
        if (o1.val < o2.val) return true;
        else if (o1.val == o2.val && o1.id < o2.id) return true;
        return false;
    }
}


class HeapTest {
    public static void main(String[] args) {
        IndexedHeap<MaxComp> maxHeap = new IndexedHeap<>(15, new MaxComp());
        IndexedHeap<MinComp> minHeap = new IndexedHeap<>(15, new MinComp());

        Pair[] pairs = new Pair[15];
        pairs[0] = new Pair(15, 0);
        pairs[1] = new Pair(11, 2);
        pairs[2] = new Pair(5, 2);
        pairs[3] = new Pair(8, 5);
        pairs[4] = new Pair(3, 3);
        pairs[5] = new Pair(2, 5);
        pairs[6] = new Pair(6, 3);
        pairs[7] = new Pair(1, 6);
        pairs[8] = new Pair(9, 6);
        pairs[9] = new Pair(10, 7);
        pairs[10] = new Pair(4, 5);
        pairs[11] = new Pair(12, 5);
        pairs[12] = new Pair(13, 6);
        pairs[13] = new Pair(14, 7);
        pairs[14] = new Pair(7, 4);

        for (int i = 0; i < 15; i++) {
//            maxHeap.add(pairs[i]);
            minHeap.add(pairs[i]);
        }

//        maxHeap.update(1, 9);
//        maxHeap.remove(13);
//        while(!maxHeap.isEmpty()) {
//            Pair pair = maxHeap.poll();
//            System.out.println(pair.id + " " + pair.val);
//        }

        minHeap.update(13, -4);
        minHeap.remove(8);
        while(!minHeap.isEmpty()) {
            Pair pair = minHeap.poll();
            System.out.println(pair.id + " " + pair.val);
        }

    }
}