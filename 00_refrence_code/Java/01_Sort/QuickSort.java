import java.util.Arrays;

class QuickSort {

    int[] arr;
    int n;

    void init(int[] _arr) {
        n = _arr.length;
        arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = _arr[i];
    }

    void sort(int s, int e) {
        if (s >= e) return;
        int pivotIdx = partitioning(s, e);
        sort(s, pivotIdx - 1);
        sort(pivotIdx + 1, e);
    }

    int partitioning(int s, int e) {
        int pivot = arr[e]; // 마지막 요소를 피벗으로 선택
        int idx = s - 1; // 피벗보다 작은 값들이 들어갈 인덱스

        for (int j = s; j < e; j++) {
            // 피벗보다 작은 값들을 swap
            if (arr[j] < pivot) {
                idx++;
                int tmp = arr[idx];
                arr[idx] = arr[j];
                arr[j] = tmp;
            }
        }
        // 피벗과 idx + 1의 위치를 서로 교환함
        int tmp = arr[idx + 1];
        arr[idx + 1] = arr[e];
        arr[e] = tmp;
        return idx + 1;
    }

    public static void main(String[] args) {
        int[] tmpArr = {-1, -3, -5, 1, 8, 9, 5, 13, 10, 8};
        QuickSort quickSort = new QuickSort();
        quickSort.init(tmpArr);
        System.out.println(Arrays.toString(quickSort.arr)); // [-1, -3, -5, 1, 8, 9, 5, 13, 10, 8]

        quickSort.sort(0, quickSort.n - 1);
        System.out.println(Arrays.toString(quickSort.arr)); // [-5, -3, -1, 1, 5, 8, 8, 9, 10, 13]
    }
}
