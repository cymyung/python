# 파일명: s0319_2.py
def average(scores):
    sum = 0
    for score in scores:
        sum += score
    avg = sum / len(scores)
    return avg

student1 = ['홍길동', 89, 93, 95, 88, 90]
student2 = ['황진이', 68, 72, 65, 60, 70]
student3 = ['멍멍이', 78, 85, 80, 88, 90]
students = [student1, student2, student3]

for name, *scores in students:
    avg = average(scores)
    print(f'{name}학생의 평균점수: {avg:.1f}점')
