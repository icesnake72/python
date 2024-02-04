'''
비밀번호를 맞혀라, 비밀번호='qwerty'
최대 5번 시도할 수 있다
5번이내에 성공하면 '비밀번호를 맞혔습니다' 를 출력
아니면 '비밀번호 입력 횟수를 초과했습니다' 를 출력
'''

correct = False
for n in range(5):
    password = input('비밀번호를 입력하세요 >>> ')
    if password=='qwerty':
        correct = True
        break
    
if correct==True:
    print('비밀번호를 맞혔습니다')
else:
    print('비밀번호 입력 횟수를 초과했습니다')
