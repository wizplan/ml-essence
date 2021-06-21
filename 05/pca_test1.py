import numpy as np
import matplotlib.pyplot as plt
import csv
import pca

# 데이터 로드
Xy = []
with open("winequality-red.csv") as fp:
    for row in csv.reader(fp, delimiter=";"):
        Xy.append(row)
Xy = np.array(Xy[1:], dtype=np.float64)
X = Xy[:, :-1]

# 학습
model = pca.PCA(n_components=2)
model.fit(X)

# 변환
Y = model.transform(X)

# 그리기
plt.scatter(Y[:, 0], Y[:, 1], color="k")
plt.show()