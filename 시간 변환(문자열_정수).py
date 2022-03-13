# 간단한 시간 변환

def strTimetoInt(str_time):  # 문자열 시간을 정수로 바꾸는 함수(분)
    str_time = list(map(int, str_time.split(":")))
    return str_time[0]*60+str_time[1]

def intTimetoStr(int_time):  # 정수 시간(분)을 글자형태로 바꾸는 함수
    hours = int_time//60
    minutes = int_time % 60
    if hours < 10:
        hours = "0"+str(hours)
    if minutes < 10:
        minutes = "0"+str(minutes)
    return str(hours)+":"+str(minutes)
