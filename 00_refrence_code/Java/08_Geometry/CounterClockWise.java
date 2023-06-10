public class CounterClockWise {

    /*
    * CCW (Counter Clock Wise)
    * ccw를 연산하는 도중에 오버 플로우가 발생할 수도 있어 long형으로 선언
    * ccw의 결과가 양수, 음수, 0인 것이 더 중요하므로 값 자체를 반환하지 않고 0, 1, -1을 반환
    * */
    static int ccw(int x1, int y1, int x2, int y2, int x3, int y3) {
        long result = (long) (x2 - x1) * (y3 - y1) - (long) (x3 - x1) * (y2 - y1);
        if (result > 0) return 1;
        else if (result < 0) return -1;
        else return 0;
    }


    /*
    * 교차 여부 판별 (ccw 활용)
    * true: 교차, false: 교차 X
    * */
    static boolean isIntersect(int x1, int y1, int x2, int y2, int x3, int y3, int x4, int y4) {
        // AB (ABC * ABD)
        int ab = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4);
        // CD (CDA * CDB)
        int cd = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2);

        // 두 선분이 일직선 상에 있을 경우
        if (ab == 0 && cd == 0) {
            // 대소 비교를 위해 점들의 위치를 변경
            int mx1 = Math.min(x1, x2);
            int my1 = Math.min(y1, y2);
            int mx2 = Math.max(x1, x2);
            int my2 = Math.max(y1, y2);

            int mx3 = Math.min(x3, x4);
            int my3 = Math.min(y3, y4);
            int mx4 = Math.max(x3, x4);
            int my4 = Math.max(y3, y4);

            // (x2, y2) >= (x3, y3) and (x4, y4) >= (x1, y1)인 경우에만 교차
            if (mx4 >= mx1 && my4 >= my1 && mx2 >= mx3 && my2 >= my3) return true;
            return false;
        }

        return ab <= 0 && cd <= 0;
    }

}
