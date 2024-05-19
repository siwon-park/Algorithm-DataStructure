# 인덱스드 힙(Indexed Heap)
last = 0


def is_empty() -> bool:
    global last
    return last == 0


def is_full() -> bool:
    global last, N
    return last == N


def add(item: tuple) -> None:  # 삽입 연산
    global last
    if is_full():
        return
    last += 1
    heap[last] = item
    memo[item[0]] = last  # item의 id의 위치를 기록
    c = last
    p = c // 2
    while p > 0 and heap[c][1] < heap[p][1]:  # 부모의 data값이 더 크다면 교환
        heap[p], heap[c] = heap[c], heap[p]  # 스왑
        # 위치 갱신
        memo[heap[p][0]] = p
        memo[heap[c][0]] = c
        c = p
        p = c // 2
    return


def poll() -> tuple:
    global last
    if is_empty():
        return ()  # 비어있으면 반환 x
    # 맨 위의 요소를 변수에 저장하고 last의 위치의 원소를 맨 위로 옮김
    top = heap[1]
    heap[1] = heap[last]
    last -= 1
    memo[heap[1][0]] = 1
    p = 1
    c = p * 2
    while c <= last:
        if c + 1 <= last and heap[c + 1][1] < heap[c][1]:
            c += 1
        if heap[c][1] < heap[p][1]:
            heap[p], heap[c] = heap[c], heap[p]  # 스왑
            memo[heap[p][0]] = p
            memo[heap[c][0]] = c
            p = c
            c = p * 2
        else:
            break

    return top


def peek() -> tuple:
    return heap[1]


def remove(idx: int) -> None:
    global last
    rm_idx = memo[idx]  # 삭제할 인덱스
    if rm_idx > last or rm_idx == 0:  # 삭제할 인덱스가 0이거나 last보다 크면 삭제 X
        return
    # 삭제할 곳을 last에 위치한 데이터로 변경
    heap[rm_idx] = heap[last]
    last -= 1
    memo[heap[rm_idx][0]] = rm_idx

    # 삭제할 인덱스부터 출발하여 힙 교환 (자식 -> 부모 방향)
    c = rm_idx
    p = c // 2
    while p > 0 and heap[c][1] < heap[p][1]:  # 부모의 data값이 더 크다면 교환
        heap[p], heap[c] = heap[c], heap[p]  # 스왑
        # 위치 갱신
        memo[heap[p][0]] = p
        memo[heap[c][0]] = c
        c = p
        p = c // 2

    # 삭제할 인덱스부터 출발하여 힙 교환 (부모 -> 자식 방향)
    p = rm_idx
    c = p * 2
    while c <= last:
        if c + 1 <= last and heap[c + 1][1] < heap[c][1]:
            c += 1
        if heap[c][1] < heap[p][1]:
            heap[p], heap[c] = heap[c], heap[p]  # 스왑
            memo[heap[p][0]] = p
            memo[heap[c][0]] = c
            p = c
            c = p * 2
        else:
            break


def update(idx: int, val: int) -> None:  # 갱신 로직의 경우 삭제 로직과 유사(값만 변경 후 재조정)
    global last
    up_idx = memo[idx]  # 갱신할 인덱스
    if up_idx > last or up_idx == 0:  # 갱신할 인덱스가 0이거나 last보다 크면 갱신 X
        return
    # 갱신할 곳의 값만 변경 (python의 경우 튜플이 불변이므로 새로 전체 값 부여)
    heap[up_idx] = (idx, val)
    
    # 갱신 인덱스부터 출발하여 힙 교환 (자식 -> 부모 방향)
    c = up_idx
    p = c // 2
    while p > 0 and heap[c][1] < heap[p][1]:  # 부모의 data값이 더 크다면 교환
        heap[p], heap[c] = heap[c], heap[p]  # 스왑
        # 위치 갱신
        memo[heap[p][0]] = p
        memo[heap[c][0]] = c
        c = p
        p = c // 2

    # 갱신 인덱스부터 출발하여 힙 교환 (부모 -> 자식 방향)
    p = up_idx
    c = p * 2
    while c <= last:
        if c + 1 <= last and heap[c + 1][1] < heap[c][1]:
            c += 1
        if heap[c][1] < heap[p][1]:
            heap[p], heap[c] = heap[c], heap[p]  # 스왑
            memo[heap[p][0]] = p
            memo[heap[c][0]] = c
            p = c
            c = p * 2
        else:
            break


lst = [4, 2, 5, 23, 10, 1, 19, 8, 7, 11, 3]
N = len(lst)
memo = [0 for _ in range(N + 1)]
heap = [(0, 0) for _ in range(N + 1)]  # (id, data)
