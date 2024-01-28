'''
3개의 정수를 입력받아서 그 중에서 가장 큰 수를 출력하세요

정수 1 입력 >>> 3 
정수 2 입력 >>> 4 
정수 3 입력 >>> 1

가장 큰 수는 4입니다 
'''

num1 = int(input('정수 1 입력 >>> '))
num2 = int(input('정수 2 입력 >>> '))
num3 = int(input('정수 3 입력 >>> '))

max_value = num1
if max_value < num2:
    max_value = num2
    
if max_value < num3:
    max_value = num3
    
print(f'가장 큰 수는 {max_value}입니다')
    
