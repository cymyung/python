# 파일명: s0318_2.py

sum = 0
for num in range(1, 101, 1):
    sum = sum + num
print(f'합계: {sum}')

scores = [89, 91, 85, 79, 93]
sum = 0
for score in scores:
    sum = sum + score
avg = sum / len(scores)
print(f'평균: {avg:.1f}점')

for x in range(2, 10, 1):
    for y in range(1, 10, 1):
        print(f'{x} x {y} = {x * y}')
    print('----------')
