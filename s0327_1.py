# 파일명: s0327_1.py
def csv_to_rows(file):
    lines = file.readlines()
    rows = []
    for line in lines:
        row = line.strip().split(',')
        rows.append(row)
    return rows

file = open('members.csv', 'r')
rows = csv_to_rows(file)
print(rows)
