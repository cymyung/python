# 파일명: s0321_bank.py

prompt = '''
1. 조회
2. 입금
3. 출금
4. 종료
원하는 거래번호는? '''

while True:
    number = int(input(prompt))
    if number == 1:
        print('입출금내역이 조회되었습니다.')
    elif number == 2:
        print('입금되었습니다.')
    elif number == 3:
        print('출금되었습니다.')
    elif number == 4:
        print('거래를 종료합니다.')
        print('안녕히 가세요.')
        break
    else:
        print('잘 못 입력하셨습니다. 다시 입력해주세요.')
