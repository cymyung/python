# 파일명: s0314_3.py

# 입력받은 평균점수에 따른 등급을 출력하는 프로그램
# 100 이하 90점이상:	A등급
#  90 미만 80점이상:	B등급
#  80 미만 70점이상:	C등급
#  70 미만 60점이상:	D등급
# 그외(60점미만):		F등급

avg = float(input("평균점수 입력: "))

if 100 >= avg >= 90:
    print(avg, "A등급")
elif avg >= 80:
    print(avg, "B등급")
elif avg >= 70:
    print(avg, "C등급")
elif avg >= 60:
    print(avg, "D등급")
else:
    print(avg, "F등급")
