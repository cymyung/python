# 파일명: s0311_2.py

avg = 87                # %d
grade = 'B'             # %s

# 평균점수는 87점이고, B등급입니다.
print('평균점수는 ' + str(avg) + '점이고, ' + grade + '등급입니다.')
print('평균점수는 ', avg, '점이고, ', grade, '등급입니다.', sep = '')
print('평균점수는 %d점이고, %s등급입니다.'%(avg, grade))
print('평균점수는 {}점이고, {}등급입니다.'.format(avg, grade))
print(f'평균점수는 {avg}점이고, {grade}등급입니다.')
