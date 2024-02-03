'''
while 반복문

while 논리식:
    명령문1
    명령문2
    명령문...
'''

i = 0
while i < 10:
    print(f'반복 {i}')
    i += 1
    
print(f'while 반복문이 종료되었습니다, i={i}')
    

until = int(input('반복 횟수를 입력하세요 >>> '))
i = 1
while i <= 100:    
    print(f'{i} / {until} 반복중...')
    i += 1
    
    