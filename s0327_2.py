# 파일명: s0327_2.py
def csv_to_rows(file):
    lines = file.readlines()
    rows = []
    for line in lines:
        row = line.strip().split(',')
        rows.append(row)
    return rows
def average(scores):
    sum = 0
    for score in scores:
        sum += int(score)
    avg = sum / len(scores)
    return avg
def grade(avg):
    if avg >= 90:   grd = 'A'
    elif avg >= 80: grd = 'B'
    elif avg >= 70: grd = 'C'
    elif avg >= 60: grd = 'D'
    else:           grd = 'E'
    return grd

for n in range(1, 4):
    file = open(f'csv/class_{n}.csv', 'r')
    rows = csv_to_rows(file)
    print(f'{n}학생들의 결과:' )
    for row in rows:
        name, addr, *scores = row
        avg = average(scores)
        grd = grade(avg)
        print(f'{name}학생의 평균: {avg:.1f}점, {grd}등급')
    print()