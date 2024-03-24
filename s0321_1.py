# 파일명: s0321_1.py

def average(scores):
    sum = 0
    for score in scores:
        sum += score
    avg = sum / len(scores)
    return avg

scores1 = [89, 91, 90, 95, 93]
avg = average(scores1)
print(f'평균점수: {avg:.1f}점')

scores2 = [45, 67, 55, 60, 47, 52]
avg = average(scores2)
print(f'평균점수: {avg:.2f}점')

scores3 = [95, 90, 80, 88]
avg = average(scores3)
print(f'평균점수: {avg:.3f}점')
