# 파일명: s0314_password.py

# 4자리 수의 암호를 입력받아 사용가능한 암호인지를 검증하는 프로그램
# 사용할 수 없는 암호의 조건들
# 1. 중복되는 수가 없어야한다.			ex) 1891, 5590, 1545
# 2. 4자리 연속 1씩 증가하면 안된다.	ex) 1234, 6789
# 3. 4자리 연속 1씩 감소하면 안된다.	ex) 9876, 6543
while True:
    password = input('4자리 수의 암호입력: ')
    p1 = int(password[0])
    p2 = int(password[1])
    p3 = int(password[2])
    p4 = int(password[3])
    duplicated = p1 == p2 or p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4 or p3 == p4
    incremented = p1 + 1 == p2 and p2 + 1 == p3 and p3 + 1 == p4
    decremented = p1 - 1 == p2 and p2 - 1 == p3 and p3 - 1 == p4
    unused_password = duplicated or incremented or decremented
    if unused_password:
        print("사용할 수 없는 암호입니다.")
    else:
        print("사용할 수 있는 암호입니다!!!")
        break