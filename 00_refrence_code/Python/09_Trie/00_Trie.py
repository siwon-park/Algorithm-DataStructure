# 트라이 구현

# 노드
class Node:

    key = None # 문자열에서 문자를 저장함
    data = None # 문자열 전체를 저장함
    child_node = None # 문자에 대한 자식 노드를 저장하기 위한 딕셔너리
    end_of_word = None # 단어의 끝인지 확인(자식 노드가 더 있는지 확인)하기 위한 변수

    def __init__(self, key):
        self.key = key
        self.child_node = dict()
        self.end_of_word = False

# 트라이
class Trie:

    root_node = None

    def __init__(self):
        self.root_node = Node(None)

    # 문자열 삽입
    def insert(self, S: str) -> None:

        node = self.root_node # 트라이의 함수 시작은 무조건 루트 노드로부터 시작함

        for s in S:
            node.child_node[s] = node.child_node.get(s, Node(s)) # 문자 s를 자식노드로 가지는 노드가 없다면 key를 s로 하여 자식 노드를 추가
            node = node.child_node[s]

        node.data = S # 맨 마지막에 문자열 전체를 저장(나중에 startswith에서 활용 가능)
        node.end_of_word = True # 문자열의 끝이므로 True

    # 찾기 함수
    def search(self, S: str) -> bool:

        node = self.root_node

        for s in S:
            if node.child_node.get(s) == None: # s를 key로 가지는 자식 노드가 없다면
                return False # False를 반환

            node = node.child_node.get(s)

        return node.end_of_word # 무조건적으로 True를 반환하면 안 됨 => 예를 들어 "kakao"라는 단어만 있는데, "kaka"를 입력해도 True를 반환하게 됨

    # 접두사로 시작하는 단어를 반환
    def startswith(self, prefix: str) -> list:

        node = self.root_node
        words = []

        for p in prefix:
            node = node.child_node.get(p)
            if node == None:
                return words # 빈 배열 반환

        node = [node]
        nxt_node = []

        while True:
            for _node in node:
                if _node.data:
                    words.append(_node.data)
                nxt_node.extend(list(_node.child_node.values())) # 자식 노드들의 노드 객체를 추가함

            if len(nxt_node): # 자식 노드가 더 있으면
                node = nxt_node
                nxt_node = []
            else:
                break
        
        return words # 해당 문자열로 시작하는 문자열 배열을 반환


