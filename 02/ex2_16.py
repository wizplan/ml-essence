with open("output.txt", "w") as fw:  # 쓰기용으로 파일 열기
    with open("sample.txt") as fr: # 읽기용으로 열기
        for line in fr:
            print(line, end="", file=fw)