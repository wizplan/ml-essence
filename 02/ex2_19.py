d = {"a": 1, "b": 2, "c": 3}

try:
    print(d["d"])  # 기본적으로 실행하는 구문
except KeyError:
    print("KeyError!")  # KeyError가 발생했을 때 실행하는 구문