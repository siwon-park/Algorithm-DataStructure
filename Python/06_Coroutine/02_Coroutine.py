# 코루틴 예시 2
# async 키워드로 선언된 코루틴을 네이티브 코루틴이라고 함(python 3.7이상부터 지원)

# async 키워드로 선언된 코루틴 함수는 일반적인 방식으로 호출할 수는 없고,
# 특수한 방식으로 호출을 해야 정상적으로 동작
# 이를 위해 존재하는 것이 Python 내장 모듈인 asyncio
import asyncio 


async def show_text():
    print("Hello World!")

loop1 = asyncio.new_event_loop() # asyncio 모듈의 event loop 객체 생성
loop1.run_until_complete(show_text()) # 코루틴 함수가 완전히 종료될 때까지 기다림
loop1.close() # event loop를 종료함


# 다른 함수 내에서 코루틴 함수 호출하기
async def cal(x, y):
    return x * y

async def main(a, b):
    ret = await cal(a, b) # 다른 함수 내에서 코루틴 함수를 호출하려면 await키워드를 사용해야함
    print(ret)

loop2 = asyncio.new_event_loop()
loop2.run_until_complete(main(2, 4))
loop2.close()

