# 코루틴 예시 1
# yield를 통해 구현한 코루틴 함수를 제네레이터 기반 코루틴이라고 함

def num_coroutine():
    while True:
        x = (yield)
        print(x)

co = num_coroutine() # co를 print하면 generator가 출력된다.
next(co) # coroutine함수를 호출함
# 함수 내부의 while True 구문의 yield까지 도착한 뒤 값이 들어올 때까지 기다림

co.send(1) # 1을 보냄 => coroutine함수에 의해 1이 출력되고 다시 yield로 가서 기다림
co.send(2) # 2를 보냄 => coroutine함수에 의해 2가 출력되고 다시 yield로 가서 기다림

