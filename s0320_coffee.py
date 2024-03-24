# 파일명: s0320_coffee.py

coffee = 5

while coffee > 0:
    money = int(input(f'동전을 넣어주세요[잔량:{coffee}]: '))
    
    if money == 300:
        print('커피를 줍니다.')
        coffee -= 1
    elif money > 300:
        change = money - 300
        print(f'거스름돈 {change}원과 커피를 줍니다.')
        coffee -= 1
    elif money < 300:
        print('동전을 그대로 돌려줍니다.')
else:
    print('커피가 모두 소진되었습니다. 판매를 중지합니다.')

