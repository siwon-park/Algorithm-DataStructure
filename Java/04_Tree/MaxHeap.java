class MaxHeap {

    int last;
    int[] heap;
    int maxSize;

    MaxHeap(int n) {
        int last = 0;
        maxSize = n;
        heap = new int[n + 1];
    }

    boolean isEmpty() {
        return last == 0;
    }

    boolean isFull() {
        return last == maxSize;
    }

    void add(int data) {
        if (isFull()) return;
        heap[++last] = data;
        int c = last;
        int p = c / 2;
        while (p > 0 && heap[p] < heap[c]) {
            swap(p, c);
            c = p;
            p = c / 2;
        }
    }

    int poll() {
        int val = heap[1];
        heap[1] = heap[last--];
        int p = 1;
        int c = 2 * p;
        while (c <= last) {
            if (c + 1 <= last && heap[c] < heap[c + 1]) c += 1;
            if (heap[p] < heap[c]) {
                swap(p, c);
                p = c;
                c = 2 * p;
            } else break;
        }
        return val;
    }

    int peek() {
        return heap[1];
    }

    void swap(int a, int b) {
        int tmp = heap[b];
        heap[b] = heap[a];
        heap[a] = tmp;
    }

    public static void main(String[] args) {
        MaxHeap maxHeap = new MaxHeap(10);

        for (int i = 0; i < 10; i++) {
            maxHeap.add(i + 1);
        }

        System.out.println(maxHeap.peek()); // 10
        System.out.println(maxHeap.isFull()); // true
        System.out.println(maxHeap.isEmpty()); // false

        while (!maxHeap.isEmpty()) {
            System.out.println(maxHeap.poll());
        }
    }
}
