// 조합(nCk) (출력이 아닌 리스트에 담음)
import java.util.ArrayList;
import java.util.Arrays;

public class Combination {

    static int N, M; // N개, M개 -> N개 중 M개를 고름
    static int[] arr; // 원본 배열
    static ArrayList<int[]> combinations; // 집합

    static void combine(int k, int s, int[] tmp) {
        if (k == M) {
            int[] copied = new int[M];
            for (int i = 0; i < M; i++) copied[i] = tmp[i]; // 복사
            combinations.add(copied);
            return;
        }
        for (int i = s; i < N; i++) {
            tmp[k] = arr[i];
            combine(k + 1, i + 1, tmp);
            tmp[k] = -1; // 정적 배열이기 때문에 사실 없어도 상관 없음
        }
    }

    public static void main(String[] args) {
        N = 5;
        M = 3;
        arr = new int[N];
        for (int i = 1; i < N + 1; i++) arr[i - 1] = i;

        combinations = new ArrayList<>();
        int[] tmp = new int[M];
        Arrays.fill(tmp, -1);
        combine(0, 0, tmp);

        System.out.println("debug Point");
    }
}

