def g(a, b=100):  # 매개변수 b에 기본값을 설정
    return a + b

print(g(3))  # 매개변수 b에 해당하는 인수를 설정하지 않음
print(g(2, 3))