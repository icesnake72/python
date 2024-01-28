# 1. 시험점수를 입력받아서...
# 100~90 : A
# 80~89 : B
# 70~79 : C
# 60~69 : D
# 그외에는 F를 출력하시요




# 점수를 입력하세요 >>> 90
# 점수는 90점이고, 학점은 A학점입니다.

score = int(input('점수를 입력하세요 >>> '))
grade = 'F'
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'

print(f'점수는 {score}점이고, 학점은 {grade}학점입니다.')

