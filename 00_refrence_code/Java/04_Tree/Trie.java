import java.util.HashMap;
import java.util.Map;

// 트라이(Trie)
class Trie {
    TrieNode root = new TrieNode();

    // 문자열 삽입
    void insert(String word) {
        TrieNode node = this.root; // 루트 노드 호출 후 문자열 삽입
        for (int i = 0; i < word.length(); i++) {
            // computeIfAbsent: key가 Map에 포함되어 있지 않은 경우, 새로운 객체를 생성하여 반환함
             node = node.childNodes.computeIfAbsent(word.charAt(i), key -> new TrieNode());
//            Character c = word.charAt(i);
//            if (node.childNodes.get(c) == null) {  // 없으면 생성
//                node.childNodes.put(c, new TrieNode());
//            }
//            node = node.childNodes.get(c);
        }
        node.isLast = true; // 마지막 문자일 경우 끝이라고 표시해줘야 함
    }

    // 문자열 탐색(경우에 따라서는 contains 메서드로 명명하기도 함)
    boolean search(String word) {
        TrieNode node = this.root; // Trie는 항상 루트부터 호출
        for (int i = 0; i < word.length(); i++) {
            node = node.childNodes.get(word.charAt(i));
            if (node == null) return false; // 노드가 null이면 트라이에 문자열이 없음
        }
        // 트라이에 저장된 것은 "busy"인데, "bus"를 찾고자 했다면, s 다음에 y를 키로 가지는 노드가 존재하므로
        // s는 "busy"의 마지막 단어가 아니므로 "bus"를 찾았을 때는 false를 반환해야 한다.
        return node.isLast;
    }

    // 문자열 삭제 연산 -> 트라이에 넣은 단어여야만 함
    // 삭제할 문자열이 있다고 해서 바로 삭제하면 안됨
    // 예) "Do"와 "Door"가 트라이에 있다고 할 때, "Do"는 "Door"의 접두사임
    // 따라서 "Door"에서 두 번째 o의 isLast를 false로 변경해야 함
    void delete(String word) {
        if (!search(word)) return; // 트라이에 단어가 없으면 삭제 불가능
        deleteWord(word, this.root, 0);
    }

    // 재귀 호출을 통해 단어를 삭제함
    void deleteWord(String word, TrieNode node, int idx) {
        if (idx == word.length()) { // 단어의 글자수와 인덱스가 일치한다면
            node.isLast = false; // 노드의 마지막 글자 유무를 false로 변경
            return;
        }
        char c = word.charAt(idx); // 현재 글자
        node = node.childNodes.get(c);
        if (node == null) return; // 만약 삭제할 단어의 끝까지 가지도 않았는데 자식이 null이면 return 함
        deleteWord(word, node, idx + 1);
        // 현재 노드의 자식이 비어있고, 해당 노드가 마지막 문자가 아니면 삭제해도 영향이 없으므로 삭제 가능 -> key중 node에 해당하는 값 삭제
        if (node.childNodes.isEmpty() && !node.isLast) node.childNodes.remove(c, node);
    }

    public static void main(String[] args) {
        // Trie 자료구조 생성
        Trie trie = new Trie();

        System.out.println("=========== 트라이에 문자열 저장 후 검색 테스트 ============");
        // Trie에 문자열 저장
        trie.insert("kakao");
        trie.insert("busy");
        trie.insert("card");
        trie.insert("cap");

        // Trie에 저장 된 문자열 확인
        System.out.println(trie.search("bus")); // false
        System.out.println(trie.search("busy")); // true
        System.out.println(trie.search("kakao")); // true
        System.out.println(trie.search("cap")); // true

        System.out.println("=======================================================");
        System.out.println("=========== 트라이에 문자열 저장 후 삭제 테스트 ============");

        trie.insert("door");
        trie.insert("do");

        System.out.println(trie.search("door")); // true
        System.out.println(trie.search("do")); // true

        trie.delete("do");
        System.out.println(trie.search("door")); // true
        System.out.println(trie.search("do")); // false

    }
}

// 트라이 구현을 위한 노드
class TrieNode {
    Map<Character, TrieNode> childNodes = new HashMap<>(); // 자식 노드
    boolean isLast; // 마지막 단어 유무 판별
}
