import java.util.Arrays;

class SelectionSort {
    int[] arr;
    int n;

    void init(int[] _arr) {
        n = _arr.length;
        arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = _arr[i];
    }

    void sort() {
        for (int i = 0; i < n - 1; i++) {
            int minIdx = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIdx]) {
                    minIdx = j;
                }
            }

            int tmp = arr[i];
            arr[i] = arr[minIdx];
            arr[minIdx] = tmp;
        }
    }

    public static void main(String[] args) {
        int[] tmpArr = {-1, -3, -5, 1, 8, 9, 5, 13, 10, 8};
        SelectionSort selectionSort = new SelectionSort();
        selectionSort.init(tmpArr);
        System.out.println(Arrays.toString(selectionSort.arr)); // [-1, -3, -5, 1, 8, 9, 5, 13, 10, 8]

        selectionSort.sort();
        System.out.println(Arrays.toString(selectionSort.arr)); // [-5, -3, -1, 1, 5, 8, 8, 9, 10, 13]

    }

}
