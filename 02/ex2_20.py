d = {"a": 1, "b": 2, "c": 3}

try:
    print(d["d"])
except KeyError as err:  # 발생한 예외 관련 메시지를 변수 err에 저장
    print("KeyError: {}".format(err))  # 에러 내용을 출력

'''
try:
    print(d["d"])
except:
    print("Something is wrong")
'''

'''
try:
    print(d["d"])
except Exception as err:
    print(type(err))
    print(err)
'''