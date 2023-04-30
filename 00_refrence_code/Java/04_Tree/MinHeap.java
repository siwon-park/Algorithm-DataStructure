class MinHeap {
    int last;
    int maxSize;
    int[] heap;

    MinHeap(int n) {
        this.last = 0;
        this.maxSize = n;
        this.heap = new int[n + 1];
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
        while (p > 0 && heap[c] < heap[p]) {
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
            if (c + 1 <= last && heap[c + 1] < heap[c]) c += 1;
            if (heap[c] < heap[p]) {
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
        MinHeap minHeap = new MinHeap(10);

        for (int i = 10; i > 0; i--) {
            minHeap.add(i);
        }

        System.out.println(minHeap.peek()); // 1
        System.out.println(minHeap.isFull()); // true
        System.out.println(minHeap.isEmpty()); // false

        while (!minHeap.isEmpty()) {
            System.out.println(minHeap.poll());
        }
    }
}