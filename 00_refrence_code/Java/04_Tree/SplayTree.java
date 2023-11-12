// 스플레이 트리
class SplayTree {
    Node root;
    SplayTree() {}
    
    // rotate: 특정 노드를 자신의 부모 위치로 올리는 함수
    void rotate(Node x) {
        Node p = x.parent; // x의 부모 노드
        // Node b = null;
        if (p == null) return; // p가 null이면 x가 루트 노드이므로 종료
        if (x == p.left) { // x가 왼쪽 자식일 경우
            p.left = x.right; // p의 왼쪽 자식을 x의 오른쪽 자식으로 변경
            if (x.right != null) {
                x.right.parent = p; // x의 오른쪽 자식이 p의 왼쪽 자식이 되었으므로 x의 오른쪽 자식의 부모는 p이다.
            }
            x.right = p; // x의 오른쪽 자식을 p로 변경
        } else { // x가 오른쪽 자식일 경우
            p.right = x.left; // p의 오른쪽 자식을 x의 왼쪽 자식으로 변경
            if (x.left != null) {
                x.left.parent = p; // 마찬가지로 x의 왼쪽 자식이 p의 오른쪽 자식이 되었으므로 x의 왼쪽 자식의 부모는 p이다.
            }
            x.left = p; // x의 왼쪽 자식을 p로 변경
        }
        // x와 p의 부모 재설정
        x.parent = p.parent; // x가 p의 위치로 갔으니 x의 부모는 p의 부모로 변경됨
        p.parent = x; // p의 부모는 x가 됨
        if (x.parent != null) { // x가 루트가 아닐 경우
            // x를 조건에 따라 x의 부모의 왼쪽/오른쪽 자식 중 하나로 변경
            if (x.parent.left == p) { // x의 부모의 왼쪽 자식이 p라면
                x.parent.left = x;
            } else {
                x.parent.right = x;
            }
        } else { // x의 부모가 없으면 x는 루트가 됨
            root = x;
        }

    }

    // splay: 특정 노드를 루트 노드 위치로 옮기는 함수
    void splay(Node x) {
        while (x.parent != null) { // x가 루트라면 종료
            Node p = x.parent; // x의 부모
            Node g = p.parent; // p의 부모; x의 조부모
            if (g != null) {
                // g-p 방향과 p-x 방향이 같으면 rotate(p)와 rotate(x)를 차례대로 수행
                if ((g.left == p && p.left == x) || (g.right == p && p.right == x)) {
                    // Zig-Zig Step
                    rotate(p);
                    rotate(x);
                } else { // 방향이 다른 경우 rotate(x)를 두 번 수행한다.
                    // Zig-Zag Step
                    rotate(x);
                    rotate(x);
                }
            } else { // p가 루트라면 rotate(x) 호출 후 종료
                rotate(x); // Zig Step
            }
        }
    }

    // insert: 삽입
    void insert(int key) {

    }

    // find: 찾기
    boolean find(int key) {
        return false;
    }

}


class Node {
    int key; // key값(data)
    Node parent, left, right;
    Node() {}
    Node(int key) {
        this.key = key;
    }
}