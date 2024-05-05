import java.util.Arrays;

class InsertionSort {

    int[] arr;
    int n;

    void init(int[] _arr) {
        n = _arr.length;
        arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = _arr[i];
    }

    void sort() {
        for (int i = 1; i < n; i++) {
            for (int j = i; j > 0; j--) {
                if (arr[j] < arr[j - 1]) {
                    // swap
                    int tmp = arr[j];
                    arr[j] = arr[j - 1];
                    arr[j - 1] = tmp;
                } else { // i 앞에는 정렬되어 있다고 가정하므로 arr[j] >= arr[j - 1]이면 break 가능
                    break;
                }
            }
        }
    }

    public static void main(String[] args) {
        int[] tmpArr = {-1, -3, -5, 1, 8, 9, 5, 13, 10, 8};
        InsertionSort insertionSort = new InsertionSort();
        insertionSort.init(tmpArr);
        System.out.println(Arrays.toString(insertionSort.arr)); // [-1, -3, -5, 1, 8, 9, 5, 13, 10, 8]

        insertionSort.sort();
        System.out.println(Arrays.toString(insertionSort.arr)); // [-5, -3, -1, 1, 5, 8, 8, 9, 10, 13]
    }
}
