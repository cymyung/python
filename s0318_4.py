# 파일명: s0318_4.py

print('코드1')
for x in [1, 2, 3, 4]:
    print(f'x = {x}')
    print(f'코드2({x})')
    if x % 2 == 0:
        continue
    print(f'코드3({x})')
print('코드4')
