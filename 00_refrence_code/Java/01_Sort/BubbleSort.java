import java.util.Arrays;

class BubbleSort {

    int[] arr;
    int n;

    void init(int[] _arr) {
        n = _arr.length;
        arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = _arr[i];
    }

    void sort() {
        for (int i = 0; i < n - 1; i++) {
            boolean swap = false;
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // swap
                    int tmp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = tmp;
                    swap = true;
                }
            }
            if (!swap) break; // 정렬을 하지 않은 곳에서 스왑된 적이 없으면 정렬된 상태기 때문에 break
        }
    }

    public static void main(String[] args) {
        int[] tmpArr = {-1, -3, -5, 1, 8, 9, 5, 13, 10, 8};
        BubbleSort bubbleSort = new BubbleSort();
        bubbleSort.init(tmpArr);
        System.out.println(Arrays.toString(bubbleSort.arr)); // [-1, -3, -5, 1, 8, 9, 5, 13, 10, 8]

        bubbleSort.sort();
        System.out.println(Arrays.toString(bubbleSort.arr)); // [-5, -3, -1, 1, 5, 8, 8, 9, 10, 13]
    }
}
