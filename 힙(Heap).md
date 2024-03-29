# 07_힙(Heap)과 우선순위 큐(Priorty Queue)

> 완전 이진 트리에 있는 노드 중에서 키 값이 가장 큰 노드나 가장 작은 노드를 찾기 위해 만든 자료 구조

## 1. 힙(Heap)

힙의 가장 대표적인 종류는 최소 힙과 최대 힙이 있다.

### 1) 최소 힙(Min Heap)

키 값이 가장 작은 노드를 찾기 위한 완전 이진 트리 자료 구조

- 부모 노드의 키 값 < 자식 노드의 키 값
- 루트 노드는 키 값이 가장 작은 노드

<br>

### 2) 최대 힙(Max Heap)

키 값이 가장 큰 노드를 찾기 위한 완전 이진 트리 자료 구조

- 부모 노드의 키 값 > 자식 노드의 키 값
- 루트 노드는 키 값이 가장 큰 노드

<br>

### 3) 연산

> 힙 연산의 기본 순서

#### 삽입

1. 삽입할 자리(last)를 확장하고(last += 1), 확장한 자리에 삽입할 원소를 저장

2. 부모의 키 값과 크기를 비교해서 부모 노드와 자리 변경(부모 노드가 없을 때까지 또는 비교 조건(부모의 키 값이 더 커야함 또는 자식의 키 값이 더 커야함)이 일치하는 동안 계속 반복)


<br>

#### 삭제

1. 변수에 반환할 루트 값을 저장
2. 루트에서 요소 삭제(last의 원소 삭제 후 해당 원소값을 루트에 위치 시킴)
3. (last -= 1을 하여 last를 앞으로 옮김)
4. 자식의 키 값과 비교하여 자리 변경(자식 노드 번호가 last 이하인 동안)
   1. 오른쪽 자식이 있는지 체크하고 오른쪽 자식이 있으면 값을 비교하여  비교 조건과 일치하면 오른쪽 자식의 위치로 옮김
   2. 비교 조건이 반대일 경우 break하여 더 이상 자리를 바꾸지 않도록 함
5. 반환할 루트 값을 반환

<br>

### 4) 힙의 성능

- 삽입과 삭제 연산: O(logn)
- 전체 정렬: O(nlogn)

<br>

## 2. 인덱스드 힙(Indexed Heap)

> 힙에서 원하는 자료를 O(logN)의 시간 복잡도로 찾거나 삭제 가능한 자료 구조

최소 우선순위 큐가 하나만 있고 우선순위 큐에 있는 숫자들을 알고 있다고 할 때, 최댓값을 제거하고자 한다면 어떻게 할 수 있을까?

- 최댓값이 나올 때까지 우선순위 큐에서 숫자들을 뽑아서 저장하고 있다가 최댓값이 나오면 삭제한 다음에 저장해뒀던 숫자들을 다시 우선순위 큐에 집어 넣는다.
  - 이 방법은 매우 비효율적인 방법으로 `O(2NlogN)`이라는 시간복잡도를 가지게 된다.
  - 만약 계속해서 입력이 주어져서 삽입 연산과 함께 최댓값을 뽑으라고 하거나, K번째 값을 뽑으라고 한다면  최악의 경우 `O(N ^ 2 * logN)`의 시간이 걸릴 수도 있다.
- Indexed Heap이나 TreeSet, TreeMap 등을 활용한다.
  - `O(logN)`의 시간 복잡도로 요소를 뽑거나 넣을 수 있다.

### 구현

Indexed Heap 구현의 핵심은 메모이제이션을 통해 힙 상에서 요소의 위치를 기억해두는 것이다.

<br>

## 3. 우선 순위 큐 응용 - 중간값 찾기

우선순위 큐 2개(최소 힙, 최대 힙)을 활용하여 중간값을 찾을 수 있다.

### 핵심

`최소 힙[0] >= 최대 힙[0]`을 유지해야 한다.

즉, 최소 힙[0] < 최대 힙[0]이라면 스왑을 통해서 `최소 힙[0] >= 최대 힙[0]`을 만족시켜야 한다.

### 주의점

단, 유의사항이 하나 있는데, 입력으로 주어지는 방식에 따라 최소 힙의 맨 위에 있는 숫자가 중간값일 수도 있고 최대 힙의 맨 위에 있는 숫자가 중간값일 수도 있다.

사실 로직에 따라 어느 한 쪽의 맨 위의 값이 중간값으로 만들 수는 있지만 차라리 이렇게 생각하는 게 훨씬 편하다.

또한 중간값이라는 게 결국 정렬했을 때 `N // 2`번째 숫자이기 때문에 실제로는 숫자가 짝수 개 들어오느냐, 홀수 개 들어오느냐에 따라 나뉜 것이다.

### CASE1: 최소 힙[0]이 중간값인 경우

초기값 1개가 주어지고, 입력으로 주어지는 숫자가 2개씩 주어져서 두 수의 대소 비교가 가능한 경우

#### 로직

- 제일 처음 주어지는 초기값은 최소 힙에 넣는다.
- 매번 입력으로 주어지는 두 수의 경우, 두 수 중 큰 수를 최소 힙에 넣고, 작은 수를 최대 힙에 넣는다.
- 만약에 최소 힙[0] < 최대 힙[0]이라면 이 조건을 만족하는 동안 스왑을 실시하여 최소 힙[0] >= 최대 힙[0]을 만족시켜 준다.
- 최소 힙[0]의 값이 중간값이다.

![image](https://github.com/siwon-park/Problem_Solving/assets/93081720/85115841-dfb6-441d-9d22-e46928eeafc0)

<br>

### CASE2: 최대 힙[0]이 중간값인 경우

초기값이 없고, 입력으로 주어지는 숫자가 1개씩이어서 두 수의 대소 비교가 불가능할 경우

#### 로직

- 만약 두 힙의 크기가 같다면 최대 힙에 숫자를 넣는다. 두 힙의 크기가 같지 않다면 최소 힙에 삽입한다.
- 만약에 최소 힙[0] < 최대 힙[0]이라면 이 조건을 만족하는 동안 스왑을 실시하여 최소 힙[0] >= 최대 힙[0]을 만족시켜 준다.
- 최대 힙[0]의 값이 중간값이다.

![image](https://github.com/siwon-park/Problem_Solving/assets/93081720/56efef54-56e7-4e3a-9828-c0b6b7ce9976)

<br>



