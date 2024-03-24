# 파일명: s0320_4.py

prompt = '원하는 작업코드[a/d/l/q]는? '


while True:
    code = input(prompt)
    if code == 'q':
        print("프로그램을 종료합니다.")
        break
    print()