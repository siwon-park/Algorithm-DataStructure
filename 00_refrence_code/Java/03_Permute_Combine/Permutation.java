// 순열(nPk) (출력이 아닌 리스트에 담음)
import java.util.ArrayList;
import java.util.Arrays;

public class Permutation {

    static int N; // N개
    // static int M; // M개 -> N개 중 M개의 순열 -> tmp 배열과 copied 배열의 길이를 M으로 선언해야 함
    static int[] arr; // 원본 배열
    static ArrayList<int[]> permutations; // 순열
    static boolean[] visited; // 방문 배열
    
    static void permute(int k, int[] tmp) {
        if (k == N) {
            int[] copied = new int[N];
            for (int i = 0; i < N; i++) copied[i] = tmp[i]; // 복사
            // System.arraycopy(tmp, 0, copied, 0, N); // 원본 배열, 원본 배열 시작 지점, 타겟 배열, 타겟 배열 시작, 끝
            permutations.add(copied);
            return;
        }
        for (int i = 0; i < N; i++) {
            if (!visited[i]) {
                visited[i] = true;
                tmp[k] = arr[i]; // tmp의 k번째 인덱스에 arr[i]를 집어 넣음
                permute(k + 1, tmp);
                tmp[k] = -1;  // 정적 배열이기 때문에 사실 없어도 상관 없음
                visited[i] = false;
            }
        }
    }

    public static void main(String[] args) {
        N = 3;
        arr = new int[N];
        visited = new boolean[N];
        for (int i = 1; i < N + 1; i++) arr[i - 1] = i;

        permutations = new ArrayList<>();
        int[] tmp = new int[N];
        Arrays.fill(tmp, -1);
        permute(0, tmp);

        System.out.println("debug Point");
    }

}
