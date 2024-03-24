# 파일명: s0314_4.py

# 3과목의 점수들을 입력받아 평균을 구하고, 평균에 따른
# 합격/불합격 여부를 출력하는 프로그램

score1 = int(input("과목1 점수입력: "))
score2 = int(input("과목2 점수입력: "))
score3 = int(input("과목3 점수입력: "))
avg = (score1 + score2 + score3) / 3

# if avg >= 60:
    # result = "합격"
# else:
    # result = "불합격"
# print(f"평균점수는 {avg:.1f}점이고, '{result}'입니다.")

if 100 >= avg >= 90: grade = "A"
elif avg >= 80:      grade = "B"
elif avg >= 70:      grade = "C"
elif avg >= 60:      grade = "D"
else:                grade = "F"
print(f"평균점수는 {avg:.1f}점이고, '{grade}'등급입니다.")
