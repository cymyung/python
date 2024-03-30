# 파일명: s0325_2.py
def average(scores):
    sum = 0
    for score in scores:
        sum += score
    avg = sum / len(scores)
    return avg
def pass_fail(avg):
    if avg >= 60: result = '합격'
    else:         result = '불합격'
    return result

students = [
             ['홍길동', 80, 89, 88, 85, 92],
             ['황진이', 93, 90, 95, 89, 90],
             ['멍멍이', 45, 55, 65, 75, 32]
           ]

for student in students:
    name, *scores = student
    avg = average(scores)
    result = pass_fail(avg)
    print(f'{name}의 평균점수는 {avg:.1f}점이고, {result}입니다.')
