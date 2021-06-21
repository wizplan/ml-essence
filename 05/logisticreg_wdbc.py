import logisticreg
import csv
import numpy as np

n_test = 100
X = []
y = []
with open("wdbc.data") as fp:
    for row in csv.reader(fp):
        if row[1] == "B":
            y.append(0)  # ❶
        else:
            y.append(1)
        X.append(row[2:])

y = np.array(y, dtype=np.float64)
X = np.array(X, dtype=np.float64)
y_train = y[:-n_test]  # ❷
X_train = X[:-n_test]
y_test = y[-n_test:]
X_test = X[-n_test:]
model = logisticreg.LogisticRegression(tol=0.01)  # ❸
model.fit(X_train, y_train)

y_predict = model.predict(X_test)  # ❹
n_hits = (y_test == y_predict).sum()
print("Accuracy: {}/{} = {}".format(n_hits, n_test, n_hits / n_test))