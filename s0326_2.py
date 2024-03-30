# 파일명: s0326_2.py

file = open('새파일.txt', 'w')
for n in range(1, 11, 1):
    line = f'{n}번째 줄입니다.\n'
    file.write(line)

file.close()
