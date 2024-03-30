# 파일명: s0325_1.py
# 4과목의 점수들을 입력받아 평균을 구하고, 
# 결과를 출력하는 프로그램

def input_scores():
    score1 = int(input("점수 입력: "))
    score2 = int(input("점수 입력: "))
    score3 = int(input("점수 입력: "))
    score4 = int(input("점수 입력: "))
    scores = [score1, score2, score3, score4]
    return scores
def average(scores):
    sum = 0
    for score in scores:
        sum += score
    avg = sum / len(scores)
    return avg
def grade(avg):
    if avg >= 90:   grd = 'A'
    elif avg >= 80: grd = 'B'
    elif avg >= 70: grd = 'C'
    elif avg >= 60: grd = 'D'
    else:           grd = 'F'
    return grd

scores = input_scores() 
avg = average(scores)
grd = grade(avg)
print(f'평균점수 {avg:.1f}점이며, {grd}등급입니다.')
