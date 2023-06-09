# KMP

`K`nuth-`M`orris-`P`ratt (크누스-모리스-프렛)

한 문자열에서 패턴이나, 부분 문자열을 찾고자할 때 사용할 수 있는 효율적인 알고리즘

<br>

## 1. 일반적인 문자열 비교

naive하게 문자열 간 비교를 한다고 할 때, 시간 복잡도는 `O(MN)`이 걸린다.

![image](https://github.com/siwon-park/Problem_Solving/assets/93081720/60291881-d975-403e-87e7-486a97290df3)

최악의 경우, N과 M이 숫자가 크다면 엄청 오래 걸릴 수 밖에 없다

<br>

## 2. KMP

그러나 KMP 알고리즘을 사용하면

`O(M + N)`에 문제를 해결할 수 있다.

### 원리

`실패 함수(failure function)`를 정의하고, `비교하는 값의 불일치가 발생했을 때 이동해야 할 위치를 기록하여 이동한 위치에서부터 비교함`

### 예시

문자열 `S`와 `W`가 있다고 할 때, S에서 W를 찾는 과정

S의 인덱스를 `i`로 하고, W의 인덱스를 `j`라고 함

![image](https://github.com/siwon-park/Problem_Solving/assets/93081720/d0fd3c3d-b846-41de-9998-348ff6901e51)

![image](https://github.com/siwon-park/Problem_Solving/assets/93081720/b721bca3-dc39-4013-809d-f37050010cb6)

![image](https://github.com/siwon-park/Problem_Solving/assets/93081720/fcfaf94a-1098-4c6f-9341-dbd0d2567d12)

![image](https://github.com/siwon-park/Problem_Solving/assets/93081720/4ece57fe-a0c5-442d-8347-1f003ec097cf)

![image](https://github.com/siwon-park/Problem_Solving/assets/93081720/0222196f-8e4e-4f07-b2f2-04e4972c85ec)

![image](https://github.com/siwon-park/Problem_Solving/assets/93081720/3284c8be-f186-4ef5-ab05-7f901af04d44)

![image](https://github.com/siwon-park/Problem_Solving/assets/93081720/ea38cfef-6633-4cfb-be3f-40a7b874c261)

<br>

### 핵심

부분 문자열의 접미사, 접두사에 대한 실패함수를 정의하고 결과값을 도출하여 갖고 있다가

![image](https://github.com/siwon-park/Problem_Solving/assets/93081720/a8c9e311-eef4-4598-8b0a-1f853f907993)

일치 실패가 발생하면 아래 표와 같이 이동시키면 된다.

![image](https://github.com/siwon-park/Problem_Solving/assets/93081720/b14ea2c8-fd49-4806-be6f-24a728bec6de)

<br>

### 실패 함수

그럼 실패 함수는 어떻게 찾을까?

놀랍게도 위에서 전체 문자열에서 KMP를 통해 부분 문자열을 찾는 과정과 동일하게 이루어진다.

부분 문자열에서 부문 문자열의 일치하는 접두/접미사의 길이를 구하면 된다.
