'''
입력된 데이터를 각각 name과 score라는 변수에 저장하는 프로그램을 만드세요.

학생의 이름과 점수를 입력하세요 >>> "김철수",85

이름은 김철수이고, 점수는 85점입니다.
'''

student = input('학생의 이름과 점수를 입력하세요 >>> ')
li = student.split(',')
name = li[0]
name = name.strip('"')
score = li[1]

print(f'이름은 {name}이고, 점수는 {score}점입니다.')


