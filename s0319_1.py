# 파일명: s0319_1.py
def compute_sum(end):
    sum = 0
    for num in range(1, end + 1, 1):
        sum = sum + num
    return sum

end = int(input('1부터 몇까지 더할까요? '))
sum = compute_sum(end)
print(f'1부터 {end}까지의 합은 {sum}입니다.')
