// 스플레이 트리
class SplayTree {
    Node root;
    SplayTree() {}
    
    // rotate; 특정 노드를 자신의 부모 위치로 올리는 함수
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

    // splay; 특정 노드를 루트 노드 위치로 옮기는 함수
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

    // insert; 삽입 -> 마지막에 삽입한 노드를 splay연산을 해줌
    void insert(int key) {
        Node newNode = new Node(key);
        if (root == null) { // 루트가 비었을 경우
            root = newNode;
            return;
        }

        Node cur = root;
        Node parent = null;
        while (cur != null) {
            parent = cur;
            if (parent.key == key) { // 중복일 경우 return
                return;
            }
            if (key < cur.key) { // 삽입하려는 key가 현재 노드보다 작으면 왼쪽으로 이동
                cur = cur.left;
            } else { // key가 현재 노드보다 크다면 오른쪽으로 이동
                cur = cur.right;
            }
        }
        // current가 null이 되는 순간 while문을 빠져나옴; current의 parent는 null이 아님.
        newNode.parent = parent;
        if (key < newNode.parent.key) {
            newNode.parent.left = newNode;
        } else {
            newNode.parent.right = newNode;
        }

        splay(newNode);
    }

    // find; 찾기 -> 마지막에 검색한 노드를 splay 연산을 해줌
    boolean find(int key) {
        if (root == null) { // 루트가 비었으면 false 반환
            return false;
        }
        Node cur = root;
        while (cur != null) {
            if (key == cur.key) break; // 탐색 성공
            if (key < cur.key) { // 찾고자 하는 key가 현재 노드의 key보다 작으면 왼쪽으로 탐색
                if (cur.left == null) { // 현재 노드의 왼쪽 자식 노드가 null이면 탐색 종료
                    break;
                }
                cur = cur.left;
            } else { // 찾고자 하는 key가 현재 노드의 key보다 크면 오른쪽으로 탐색
                if (cur.right == null) { // 현재 노드의 오른쪽 자식 노드가 null이면 탐색 종료
                    break;
                }
                cur = cur.right;
            }
        }
        
        splay(cur); // 마지막에 탐색한 노드를 루트로 이동
        return key == cur.key;
    }

    // delete; 특정 key값을 가진 노드를 삭제 -> 삭제할 노드를 splay한 다음에 삭제.
    // 단 자식이 1개 이하면 바로 삭제하지만, 자식이 2개라면 서브 트리를 합치는 과정이 필요함
    void delete(int key) {
        if (!find(key)) { // 찾고자하는 키가 없으면 탐색 종료
            return;
        }
        // find 메서드에서 이미 splay연산을 한 상태이기 때문에 별도의 splay 연산이 필요 없음
        Node p = root;
        if (p.left != null && p.right != null) { // 왼쪽, 오른쪽 서브 트리가 모두 존재하는 경우
            // 왼쪽 서브 트리를 루트로 만듦
            root = p.left;
            root.parent = null;

            // 오른쪽 서브 트리를 왼쪽 서브 트리 아래에 삽입(왼쪽 서브 트리의 오른쪽에 삽입)
            Node x = root;
            while (x.right != null) {
                x = x.right;
            }
            x.right = p.right;
            p.right.parent = x;
            return;
        }
        if (p.left != null) { // 왼쪽 자식만 있는 경우, 왼쪽 자식을 루트로 만들고 return
            root = p.left;
            root.parent = null;
            return;
        }
        if (p.right != null) { // 오른쪽 자식만 있는 경우, 오른쪽 자식을 루트로 만들고 return
            root = p.right;
            root.parent = null;
            return;
        }
        
        // 자신(루트)밖에 없을 경우 루트를 삭제
        root = null;
        return;
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