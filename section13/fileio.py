'''
파일 입출력

파일 종류: 텍스트 파일(Text File), 바이너리 파일(Binary File)

파일 입력 : 파일로부터 데이터를 읽는것 (Read File, Load)
파일 출력 : 데이터를 파이엘 저장하는것 (Write File, Save)

파일을 연다(읽기 또는 쓰기 모드 중 한가지 방법으로만 열 수 있다)
파일에 쓴다(또는 파일로부터 읽는다)
파일을 닫는다

File Mode
r : 읽기 모드
w : 쓰기 모드
a : 추가 모드

t : 텍스트 모드
b : 바이너리 모드
'''

# path : file 위치 + 파일명

# 파일 출력
file = open('파일명', 'wt')
file.write('data')
file.write('data')
file.write('data')
file.write('data')
file.write('data')
file.close()

# 파일 입력
file = open('파일명', 'r')
file.read()
file.close()

with open('파일명', 'r') as file:
    file.read()
    
# with문을 빠져나오면 file.close()를 자동으로 해준다



