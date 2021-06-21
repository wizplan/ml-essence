import csv  # csv 모듈 불러오기

s = 0
with open("sample.csv") as f:
    reader = csv.reader(f)  # csv 파일 읽기
    next(reader)  # 첫 번째 행 건너 뛰기
    for row in reader:
        s += int(row[1])  # 왼쪽에서 두 번째 열의 숫자를 모두 더함

print(s)