# 파일명: s0311_1.py

avg = 89.135
min = 1
sec = 25

print('평균점수는 ' + str(round(avg, 2)) + '점입니다.')
print('평균점수는 ', round(avg, 2), '점입니다.', sep = '')
print('평균점수는 %.2f점입니다.'%(avg))
print('평균점수는 {:.2f}점입니다.'.format(avg))
print(f'평균점수는 {avg:.2f}점입니다.')

# 잠수시간은 / min / 분 / sec / 초입니다.
# 잠수시간은 1분 25초입니다.
print('잠수시간은 ' + str(min) + '분 ' + str(sec) + '초입니다.')
print('잠수시간은 ', min, '분 ', sec, '초입니다.', sep = '')
print('잠수시간은 %d분 %d초입니다.'%(min, sec))
print('잠수시간은 {}분 {}초입니다.'.format(min, sec))
print(f'잠수시간은 {min}분 {sec}초입니다.')
