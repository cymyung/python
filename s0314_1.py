# 파일명: s0314_1.py
# 현재 소지한 현금을 입력받아 택시의 기본요금이상을 소지하고 있다면,
# 택시를 타고가고, 아니라면 걸어가라는 프로그램

money = int(input("소지한 금액: "))
card  = input("카드 소지여부[yes/no]: ")
    
if money >= 5000 or card == "yes":
    print("택시를 타고 가라.")
else:
    print("걸어 가라")
