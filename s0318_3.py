# 파일명: s0318_3.py

print('코드1')
for x in [1, 2, 3, 'a', 5]:
    print(f'x = {x}')
    print(f'코드2({x})')
    print(f'코드3({x})')
    if type(x) != type(int()):
        break
    print(f'코드4({x})')
print('코드5')
