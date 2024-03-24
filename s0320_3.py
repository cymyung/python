# 파일명: s0320_3.py

prompt = '''1. 추가
2. 제거
3. 확인
4. 종료
원하는 작업번호는? '''

while True:
    number = int(input(prompt))
    if number in [1, 2, 3]:
        print('작업이 실행되었습니다.', end = '\n\n')
    else:
        print('프로그램을 종료합니다.')
        break