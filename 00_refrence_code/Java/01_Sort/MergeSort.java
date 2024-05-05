import java.util.Arrays;

class MergeSort {

    int[] arr; // 원본 배열
    int n;
    int[] tmp; // 임시 배열

    void init(int[] _arr) {
        n = _arr.length;
        arr = new int[n];
        tmp = new int[n];
        for (int i = 0; i < n; i++) arr[i] = _arr[i];
    }

    void sort(int start, int end) {
        if (start >= end) return;
        int mid = (start + end) / 2;
        sort(start, mid);
        sort(mid + 1, end);
        merge(start, end);
    }

    void merge(int start, int end) {
        int mid = (start + end) / 2;
        int i = start; // 왼쪽으로 나눴을 때의 가장 작은 인덱스
        int j = mid + 1; // 오른쪽으로 나눴을 때의 가장 작은 인덱스
        int k = 0; // 임시 배열의 인덱스 -> start로 시작해도 됨. 단, 아래에서 원본으로 옮길 때 arr[i] = tmp[i]임.

        // 왼쪽, 오른쪽 비교해서 작은 것부터 임시 배열에 복사
        while (i <= mid && j <= end) {
            if (arr[i] <= arr[j]) tmp[k++] = arr[i++];
            else tmp[k++] = arr[j++];
        }

        // 왼쪽의 남은 부분을 임시 배열에 복사
        while (i <= mid) tmp[k++] = arr[i++];

        // 오른쪽의 남은 부분을 임시 배열에 복사
        while (j <= end) tmp[k++] = arr[j++];

        // 임시 배열의 데이터를 원본 배열로 옮김
        for (i = start; i <= end; i++) arr[i] = tmp[i - start]; // k = start였을 경우 arr[i] = tmp[i]
    }

    public static void main(String[] args) {
        int[] tmpArr = {-1, -3, -5, 1, 8, 9, 5, 13, 10, 8};
        MergeSort mergeSort = new MergeSort();
        mergeSort.init(tmpArr);
        System.out.println(Arrays.toString(mergeSort.arr)); // [-1, -3, -5, 1, 8, 9, 5, 13, 10, 8]

        mergeSort.sort(0, mergeSort.arr.length - 1);
        System.out.println(Arrays.toString(mergeSort.arr)); // [-5, -3, -1, 1, 5, 8, 8, 9, 10, 13]
    }
}
