// 중복 순열
import java.util.ArrayList;
import java.util.Arrays;

public class Production {

    static int N; // N개
    static int[] arr; // 원본 배열
    static ArrayList<int[]> productions; // 중복 순열


    static void product(int k, int[] tmp) {
        if (k == N) {
            int[] copied = new int[N];
            System.arraycopy(tmp, 0, copied, 0, N); // 원본 배열, 원본 배열 시작 지점, 타겟 배열, 타겟 배열 시작, 끝
            productions.add(copied);
            return;
        }
        for (int i = 0; i < N; i++) {
            tmp[k] = arr[i]; // tmp의 k번째 인덱스에 arr[i]를 집어 넣음
            product(k + 1, tmp);
        }
    }

    public static void main(String[] args) {
        N = 3;
        arr = new int[N];
        for (int i = 1; i < N + 1; i++) arr[i - 1] = i;

        productions = new ArrayList<>();
        int[] tmp = new int[N];
        Arrays.fill(tmp, -1);
        product(0, tmp);

        System.out.println("debug Point");
    }

}
