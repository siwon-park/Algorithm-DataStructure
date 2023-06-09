// KMP(Knuth–Morris–Pratt)
import java.util.ArrayList;

public class KMP {

    static int N, M; // S의 길이, W의 길이

    /*
    * 실패 함수 -> 불일치가 발생했을 때, 어느 위치로 이동해야 하는지를 반환 (일치하는 접두/접미사의 최대 길이)
    * */
    static int[] fail(String W) {
        int[] _fail = new int[M];
        int j = 0; // W의 인덱스 -> 사실 실패 함수는 W와 W간의 KMP를 하는 것
        for (int i = 1; i < M; i++) { // i = 0 이면 p[i] == p[j]이기 때문
            while (j > 0 && W.charAt(i) != W.charAt(j)) {
                j = _fail[j - 1]; // 불일치 발생 시 fail 배열에 기록된 숫자만큼 건너뜀
            }
            if (W.charAt(i) == W.charAt(j)) {
                // 불일치가 발생했을 경우 이동해야할 위치를 기록 (j번 째까진 일치했으니 실패 시 j + 1인 곳으로 이동)
                j += 1;
                _fail[i] = j;
            }
        }
        return _fail;
    }

    /*
    * S에서 W가 시작 인덱스가 담긴 리스트를 반환
    * */
    static ArrayList<Integer> search(String S, String W) {
        ArrayList<Integer> result = new ArrayList<>();
        int[] _fail = fail(W);
        int j = 0; // W의 인덱스
        for (int i = 0; i < N; i++) { // i는 S의 인덱스
            while (j > 0 && S.charAt(i) != W.charAt(j)) {
                j = _fail[j - 1];
            }
            if (S.charAt(i) == W.charAt(j)) { // 일치할 경우 (1)
                if (j == M - 1) { // j가 0에서 출발해서 M - 1까지 왔다면, 길이 M 동안 일치했다는 의미이므로 패턴이 매칭됨 (3)
                    result.add(i - M + 1); // i에서 M - 1을 뺀 곳이 매칭되는 패턴의 시작 위치
                    j = _fail[j];
                } else { // j가 M - 1이 아니면 아직 M만큼 오지 않았으므로 j를 증가 (2)
                    j += 1;
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        // 예시1
        String s1 = "abc abcdab abcdabcdabde";
        String w1 = "abcdabd"; // s1의 15번째 인덱스부터 일치하기 시작

        N = s1.length();
        M = w1.length();

        System.out.println(search(s1, w1)); // [15]

        // 예시2
        String s2 = "abcdeabcfabcdabc";
        String w2 = "abcdabc"; // s2의 9번째 인덱스부터 일치하기 시작

        N = s2.length();
        M = w2.length();

        System.out.println(search(s2, w2)); // [9]
    }
}