f = open("sample.txt")  # 파일 열기

for line in f:  # 1행씩 저장
    line = line.rstrip()  # 뒷 부분에 있는 공백과 줄 바꿈 제거
    print(line)

f.close()  # 파일 닫기