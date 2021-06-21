import csv

data = [[1, "a", 1.1]  # 리스트를 요소로 포함하는 리스트 생성
        [2, "b", 1.2],
        [3, "c", 1.3]]

with open("output.csv", "w") as f:
    wr = csv.writer(f)  # csv 파일에 저장
    for row in data:
        wr.writerow(row