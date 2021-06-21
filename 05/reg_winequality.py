import linearreg
import numpy as np
import csv

# 데이터 로드
Xy = []
with open("winequality-red.csv") as fp:
    for row in csv.reader(fp, delimiter=";"):  # ❶
        Xy.append(row)
Xy = np.array(Xy[1:], dtype=np.float64)  # ❷

# 데이터 세트를 훈련 데이터와 테스트 데이터로 나눔
np.random.seed(0)
np.random.shuffle(Xy)
train_X = Xy[:-1000, :-1]
train_y = Xy[:-1000, -1]
test_X = Xy[-1000:, :-1]
test_y = Xy[-1000:, -1]

# 학습하기
model = linearreg.LinearRegression()
model.fit(train_X, train_y)

# 테스트 데이터에 모델을 적용해 예측
y = model.predict(test_X)

print("처음 5개 데이터의 정답과 예측값: ")
for i in range(5):
    print("{:1.0f} {:5.3f}".format(test_y[i], y[i]))
print()
print("RMSE: ", np.sqrt(((test_y - y)**2).mean()))