# 파일명: s0320_2.py

prompt = '''1. 추가
2. 제거
3. 확인
4. 종료
원하는 작업번호는? '''

number = int(input(prompt))
while number != 4:
    print('작업이 실행되었습니다.', end = '\n\n')
    number = int(input(prompt))
print('프로그램을 종료합니다.')

    