# 파일명: s0326_1.py

A = [1, 3, 5, 7, 9]
x = 10
y = 3
try:
    del A[4]
    print( A[4] )
    print( x / y )
except IndexError:
    print('없는 위치의 index입니다.')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except:
    print('예상외의 에러입니다.')
else:
    print('에러가 발생하지 않았습니다.')
finally:
    print('이 코드는 반드시 실행됩니다.')
