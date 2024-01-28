'''
조건문(if statement)
'''
num1 = 10
num2 = 5
if num1==10 and num2==5: 
    # 코드블록이 만들어 지면서
    # 위 조건문이 참일때 분기된다.
    print(num1)
    print(num2)       
    
print('조건문 처리가 끝났습니다')


if num1==10:
    print(f'{num1}의 값은 10입니다')
else:
    print(f'{num1}의 값은 10이 아닙니다')

isOk = True
li = [] # 빈 리스트
nothing = ""
num1 = 0

if isOk:
    print(isOk)
    
if li:      # if문의 조건으로 사용될 수 있고, 빈 리스트의 논리값은 False
    print(li)
    
if nothing: # 빈 문자열의 논리값은 False이다 
    print(nothing)
    
if num1:    # 정수 0의 논리값은 False이다
    print(num1)
    
    
num1 = 10
if num1==0:
    print('num1은 0입니다')
elif num1==1:
    print('num1은 1입니다')
elif num1==2:
    print('num1은 2입니다')
elif num1==3:
    print('num1은 3입니다')
elif num1==4:
    print('num1은 4입니다')
elif num1==5:
    print('num1은 5입니다')
else:
    print('num1의 값을 알 수 없습니다')
    
    
if num1==10:
    if num2==5:
        print(num1)
        print(num2)
    else:
        print('num1은 10이고 num2는 5가 아님')
else:
    print('num1은 10이 아님')
    