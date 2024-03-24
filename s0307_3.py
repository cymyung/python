# 파일명: s0307_3.py

#       0123456789012
text = '20240307Rainy'
date = text[:8]
weather = text[8:]

print("날짜: ", date)
print("날씨: ", weather)

#      01234567890123
rrn = '981207-1234567'
year = '19' + rrn[0:2]
date = rrn[2:6]
print("주민등록번호: ", rrn)
print('------------')
print('  결    과')
print('------------')
print("생년: ", year)
print("생일: ", date)
