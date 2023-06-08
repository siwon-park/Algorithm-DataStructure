// 중복 조합(nHk) (출력이 아닌 리스트에 담음)
import java.util.ArrayList;
import java.util.Arrays;

public class CombineWithReplacement {

    static int N, M; // N개, M개 -> N개 중 M개를 고름
    static int[] arr; // 원본 배열
    static ArrayList<int[]> combinations; // 중복 집합

    static void combineWithReplace(int k, int s, int[] tmp) {
        if (k == M) {
            int[] copied = new int[M];
            System.arraycopy(tmp, 0, copied, 0, M); // 복사
            combinations.add(copied);
            return;
        }
        for (int i = s; i < N; i++) {
            tmp[k] = arr[i];
            combineWithReplace(k + 1, i, tmp);
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
        combineWithReplace(0, 0, tmp);

        System.out.println("debug Point");
    }
}

